def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2

    return True


n = int(input("Enter an integer: "))

print("Prime" if is_prime(n) else "Not prime")
