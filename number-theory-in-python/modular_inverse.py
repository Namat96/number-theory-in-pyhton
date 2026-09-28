def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return g, x, y


def modular_inverse(a, n):
    g, x, _ = extended_gcd(a, n)

    if g != 1:
        return None

    return x % n


a = int(input("Enter a: "))
n = int(input("Enter modulus: "))

inverse = modular_inverse(a, n)

if inverse is None:
    print("No modular inverse exists.")
else:
    print("Modular inverse:", inverse)
