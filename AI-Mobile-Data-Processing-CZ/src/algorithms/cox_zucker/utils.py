 
# cox_zucker/utils.py

def gcd(a, b):
    """Compute the greatest common divisor (GCD) of two numbers."""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Compute the extended GCD of two numbers."""
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def modular_inverse(a, m):
    """
    Compute the modular multiplicative inverse of 'a' modulo 'm'.
    Assumes that 'a' and 'm' are coprime.
    """
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"The numbers {a} and {m} are not coprime.")
    else:
        return (x % m + m) % m

# Other utility functions relevant to the Cox–Zucker algorithm could be included here
