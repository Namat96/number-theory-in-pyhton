# Modular Inverse using simple method
# (a × x) mod m = 1

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


a = int(input("Enter a: "))
m = int(input("Enter modulus m: "))

inv = mod_inverse(a, m)

if inv is None:
    print("Modular inverse does not exist.")
else:
    print("Modular inverse is:", inv)
