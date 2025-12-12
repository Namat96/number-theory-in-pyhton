def multiplicative_order(a, n):
    if __import__("math").gcd(a, n) != 1:
        return None

    value = 1
    for k in range(1, n + 1):
        value = (value * a) % n
        if value == 1:
            return k

    return None


def is_primitive_root(g, p):
    order = multiplicative_order(g, p)
    return order == p - 1


p = int(input("Enter a prime p: "))
g = int(input("Enter candidate g: "))

print("Primitive root:", is_primitive_root(g, p))
