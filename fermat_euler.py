from euler_phi import euler_phi


a = int(input("Enter a: "))
n = int(input("Enter n: "))

if a % n == 0:
    print("Choose a different a for this demonstration.")
else:
    print("a^phi(n) mod n =", pow(a, euler_phi(n), n))

print("For a prime p, Fermat's theorem gives a^(p-1) = 1 mod p")
