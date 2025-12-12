# Quick review of common number-theory operations in Python.

a = 17
b = 5
n = 23

print("GCD:", __import__("math").gcd(a, b))
print("a mod n:", a % n)
print("a^b mod n:", pow(a, b, n))
print("Factors of 60:", [d for d in range(1, 61) if 60 % d == 0])

print("\nThis file is only a small review before moving to larger cryptography projects.")
