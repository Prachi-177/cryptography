def extended_gcd(a, b):
    # Base case
    if b == 0:
        return a, 1, 0
    
    # Recursive case
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y

# Example usage:
a=int(input("enter first number"))
b=int(input("enter second number"))
gcd, x, y = extended_gcd(a, b)
print(f"The GCD of {a} and {b} is: {gcd}")
print(f"x = {x}, y = {y}")
print(f"{a}*{x} + {b}*{y} = {gcd}")