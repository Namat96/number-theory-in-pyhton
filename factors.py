def factors(n):
    result = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            result.append(i)
    return result


n = int(input("Enter a positive integer: "))
print("Factors:", factors(n))
