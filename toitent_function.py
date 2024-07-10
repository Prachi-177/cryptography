def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def totient(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count

# Example usage
n = 10
print(f"The totient function of {n} is {totient(n)}")