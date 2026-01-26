# Fermat's Little Theorem
# a^(p-1) ≡ 1 (mod p) when p is prime

import math


def is_prime(p):
    if p <= 1:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True


def fermat_theorem(a, p):
    if not is_prime(p):
        return "p is not prime, theorem does not apply."

    if math.gcd(a, p) != 1:
        return "a and p are not coprime."

    result = pow(a, p - 1, p)

    if result == 1:
        return "Fermat's theorem verified."
    else:
        return "Fermat's theorem failed."


# -------- MAIN PROGRAM --------

print("Fermat's Little Theorem Program")
print("-------------------------------")

a = int(input("Enter value of a: "))
p = int(input("Enter value of p (prime): "))

print(fermat_theorem(a, p))
