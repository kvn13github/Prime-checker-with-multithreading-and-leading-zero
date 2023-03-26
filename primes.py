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

print("Highest prime:", max_prime)
print("Lower primes:", lower_primes)
print("Sophie Germain primes:")
for p in lower_primes:
    if is_sophie_germain_prime(p):
        print(p)
print("Safe primes:")
for p in lower_primes:
    if is_safe_prime(p):
        print(p, end=" ")
        q = (p - 1) // 2
        if is_prime(q):
            print("(safe prime)")
        else:
            print("(not safe prime)")

