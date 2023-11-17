from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Authentication function (dummy example)
def authenticate_user(username, password):
    # Validate username and password (Replace with your authentication logic)
    valid_username = 'example_user'
    valid_password = 'example_password'
    return username == valid_username and password == valid_password

# Endpoint to receive and store authenticated mobile data
@app.route('/store_data', methods=['POST'])
def store_mobile_data():
    try:
        auth = request.authorization
        if not auth or not authenticate_user(auth.username, auth.password):
            return jsonify({'message': 'Authentication failed'}), 401

        data = request.get_json()  # Assuming data is sent in JSON format
        if not data or 'device_id' not in data or 'sensor_data' not in data:
            return jsonify({'message': 'Invalid data format'}), 400

        # Connect to the SQLite database
        conn = sqlite3.connect('database/mobile_data.db')
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS MobileData (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            device_id TEXT,
                            sensor_data TEXT
                        )''')

        # Insert received data into the database
        cursor.execute('''INSERT INTO MobileData (device_id, sensor_data)
                          VALUES (?, ?)''', (data['device_id'], data['sensor_data']))

        conn.commit()
        conn.close()
        return jsonify({'message': 'Data stored successfully'}), 200

    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Running the Flask app in debug mode
 
