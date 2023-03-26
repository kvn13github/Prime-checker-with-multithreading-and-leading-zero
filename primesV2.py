import math
from concurrent.futures import ThreadPoolExecutor

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_highest_prime(num_digits):
    upper_limit = int('9' * num_digits)
    lower_limit = int('1' + '0' * (num_digits - 1))
    for n in range(upper_limit, lower_limit - 1, -1):
        if is_prime(n):
            return n
    return None

def find_lower_primes(highest):
    lower_primes = []
    for n in range(2, highest):
        if is_prime(n):
            lower_primes.append(str(n).zfill(len(str(highest))))
    return lower_primes

if __name__ == '__main__':
    num_digits = int(input('Enter the number of digits: '))

    with ThreadPoolExecutor() as executor:
        highest_thread = executor.submit(find_highest_prime, num_digits)
        highest = highest_thread.result()

        lower_thread = executor.submit(find_lower_primes, highest)
        lower_primes = lower_thread.result()

    print(f'Highest prime: {str(highest).zfill(num_digits)}')
    print(f'Lower primes: {lower_primes}')

    sophie_germain = []
    safe_primes = []
    for p in lower_primes:
        p = int(p)
        if is_prime(2 * p + 1):
            sophie_germain.append(p)
            if is_prime((2 * p + 1) // 2):
                safe_primes.append(p)

    print('Checking for Sophie Germain and safe primes...')
    for p in sophie_germain:
        print(f'{str(p).zfill(num_digits)} is a Sophie Germain prime')
    for p in safe_primes:
        print(f'{str(p).zfill(num_digits)} is a Sophie GermainSafe prime')
