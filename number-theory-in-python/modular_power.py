def modular_power(a, e, n):
    result = 1
    a %= n

    while e > 0:
        if e % 2 == 1:
            result = (result * a) % n

        a = (a * a) % n
        e //= 2

    return result


a = int(input("Enter base: "))
e = int(input("Enter exponent: "))
n = int(input("Enter modulus: "))

print("Result:", modular_power(a, e, n))
