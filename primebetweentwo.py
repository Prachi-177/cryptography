def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = []
    for p in range(2, limit + 1):
        if is_prime[p]:
            prime_numbers.append(p)
    return prime_numbers

def primes_between(a, b):
    if a > b:
        a, b = b, a
    limit = max(a, b)
    primes = sieve_of_eratosthenes(limit)
    primes_in_range = [p for p in primes if a <= p <= b]
    return primes_in_range

# Example usage
a = 10
b = 50
print(f"Prime numbers between {a} and {b} are: {primes_between(a, b)}")
