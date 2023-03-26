import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_sophie_germain_prime(p):
    if not is_prime(p):
        return False
    q = 2 * p + 1
    return is_prime(q)

def is_safe_prime(p):
    if not is_prime(p):
        return False
    q = (p - 1) // 2
    return is_prime(q)

n = int(input("Enter the number of digits: "))
start = 10 ** (n - 1)
end = 10 ** n - 1

max_prime = None
lower_primes = []

for p in range(start, end + 1):
    if is_prime(p):
        max_prime = p
        lower_primes.append(p)

lower_primes = lower_primes[:-1]  # Exclude the highest prime

print("Highest prime: {}".format(max_prime))
print("Lower primes: {}".format(lower_primes))
print("Sophie Germain primes: 2*p + 1")
for p in lower_primes:
    if is_sophie_germain_prime(p):
        print("{} ({} is prime)".format(2*p + 1, p))
print("Safe primes: p = 2*q + 1")
for p in lower_primes:
    if is_safe_prime(p):
        q = (p - 1) // 2
        if is_prime(q):
            print("{} ({} is prime)".format(p, q))
        else:
            print("{} ({} is not prime)".format(p, q))
