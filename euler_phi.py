def euler_phi(n):
    result = n
    p = 2
    value = n

    while p * p <= value:
        if value % p == 0:
            while value % p == 0:
                value //= p
            result -= result // p
        p += 1

    if value > 1:
        result -= result // value

    return result


n = int(input("Enter n: "))
print("phi(n) =", euler_phi(n))
