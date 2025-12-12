def legendre_symbol(a, p):
    a %= p

    if a == 0:
        return 0

    value = pow(a, (p - 1) // 2, p)

    if value == 1:
        return 1
    if value == p - 1:
        return -1

    return 0


a = int(input("Enter a: "))
p = int(input("Enter an odd prime p: "))

print("Legendre symbol:", legendre_symbol(a, p))
