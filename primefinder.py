import random

def power(x, y, p):
    """
    Calculate (x^y) % p in logarithmic time.
    """
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def miller_rabin_test(d, n):
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def is_prime(n, k=5):
    if n <= 1 or n == 4:
        return False, None
    if n <= 3:
        return True, None
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for _ in range(k):
        if not miller_rabin_test(d, n):
            factor = pollards_rho(n)
            return False, factor
    return True, None

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def f(x, n):
    return (x*x + 1) % n

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x, y, d = 2, 2, 1
    while d == 1:
        x = f(x, n)
        y = f(f(y, n), n)
        d = gcd(abs(x-y), n)
    return d

# ------------------------------
# MARKED AREA: ENTER YOUR NUMBER
# ------------------------------
number_to_test = (2**2018) + 1

# Testing for primality and attempting to find a factor if composite
is_prime_result, factor = is_prime(number_to_test)
if is_prime_result:
    print(f"{number_to_test} is prime.")
else:
    print(f"{number_to_test} is not prime. A factor: {factor}")
