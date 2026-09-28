def is_quadratic_residue(a, p):
    a %= p

    for x in range(p):
        if (x * x) % p == a:
            return True

    return False


a = int(input("Enter a: "))
p = int(input("Enter an odd prime p: "))

print("Quadratic residue:", is_quadratic_residue(a, p))
