def fermat_test(a, p):
    """
    Returns True if p is probably prime based on Fermat's Little Theorem with base a.
    Returns False if p is definitely not prime.
    """
    if p <= 1:
        return False
    return pow(a, p - 1, p) == 1

def is_prime(p, k=5):
    """
    Use Fermat's test k times to check if p is probably prime.
    """
    if p <= 1:
        return False
    for _ in range(k):
        a = random.randint(2, p - 2)
        if not fermat_test(a, p):
            return False
    return True

# Example usage
import random

n = 97
print(f"{n} is probably prime: {is_prime(n)}")
