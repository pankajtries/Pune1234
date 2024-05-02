import math

def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_prime_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            if is_prime(num):
                return num
            else:
                print("Please enter a prime number.")
        except ValueError:
            print("Please enter a valid integer.")

p = get_prime_input("Enter prime number p: ")
q = get_prime_input("Enter prime number q: ")

n = p * q
phi = (p - 1) * (q - 1)

e = int(input("Enter public exponent e (such that gcd(e, phi) = 1): "))
while math.gcd(e, phi) != 1:
    print("Please enter a valid public exponent e such that gcd(e, phi) = 1.")
    e = int(input("Enter public exponent e: "))

msg = int(input("Enter the message to encrypt: "))

d = pow(e, -1, phi)

C = pow(msg, e, n)
decrypted_message = pow(C, d, n)

print("Encrypted message:", C)
print("Decrypted message:", decrypted_message)

"""
Enter prime number p: 11
Enter prime number q: 13
Enter public exponent e (such that gcd(e, phi) = 1): 23
Enter the message to encrypt: 2
Encrypted message: 85
Decrypted message: 2
"""
