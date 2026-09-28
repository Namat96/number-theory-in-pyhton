def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def inverse(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("No inverse exists")
    return x % m


# Small educational RSA example.
p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = inverse(e, phi)

message = 65
encrypted = pow(message, e, n)
decrypted = pow(encrypted, d, n)

print("n =", n)
print("phi(n) =", phi)
print("Public key =", (e, n))
print("Private key =", (d, n))
print("Message =", message)
print("Encrypted =", encrypted)
print("Decrypted =", decrypted)
