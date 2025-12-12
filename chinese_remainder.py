def crt(a1, n1, a2, n2):
    # This simple version assumes gcd(n1, n2) = 1.
    for x in range(a1, n1 * n2, n1):
        if x % n2 == a2:
            return x
    return None


a1 = int(input("x mod n1 = a1, enter a1: "))
n1 = int(input("Enter n1: "))
a2 = int(input("x mod n2 = a2, enter a2: "))
n2 = int(input("Enter n2: "))

answer = crt(a1, n1, a2, n2)

if answer is None:
    print("No solution found.")
else:
    print("Smallest non-negative solution:", answer)
