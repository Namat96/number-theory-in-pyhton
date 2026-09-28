def is_divisible(a, b):
    if b == 0:
        return False
    return a % b == 0


a = int(input("Enter a number: "))
b = int(input("Enter divisor: "))

if is_divisible(a, b):
    print(a, "is divisible by", b)
else:
    print(a, "is not divisible by", b)
