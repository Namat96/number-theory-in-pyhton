def discrete_log(g, h, p):
    value = 1

    for x in range(p):
        if value == h % p:
            return x
        value = (value * g) % p

    return None


g = int(input("Enter base g: "))
h = int(input("Enter target h: "))
p = int(input("Enter modulus p: "))

answer = discrete_log(g, h, p)

if answer is None:
    print("No small discrete logarithm found.")
else:
    print("x =", answer)
    print("Check:", pow(g, answer, p))
