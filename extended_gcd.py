def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return old_r, old_s, old_t


a = int(input("Enter a: "))
b = int(input("Enter b: "))

g, x, y = extended_gcd(a, b)

print("GCD:", g)
print("x:", x)
print("y:", y)
print("Check:", a * x + b * y)
