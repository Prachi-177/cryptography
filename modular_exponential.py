def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # In case base is larger than modulus

    while exponent > 0:
        # If exponent is odd, multiply base with result
        if (exponent % 2) == 1:
            result = (result * base) % modulus

        # Exponent must be even now
        exponent = exponent >> 1  # Divide exponent by 2
        base = (base * base) % modulus  # Square the base

    return result

# Example usage
base = 2
exponent = 10
modulus = 1000
print(f"The result of {base}^{exponent} % {modulus} is {modular_exponentiation(base, exponent, modulus)}")
