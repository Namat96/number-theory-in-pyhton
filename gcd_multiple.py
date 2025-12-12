from gcd import gcd


numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

result = numbers[0]
for number in numbers[1:]:
    result = gcd(result, number)

print("GCD:", result)
