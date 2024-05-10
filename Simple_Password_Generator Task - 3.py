import secrets
import string

alphabet = string.ascii_letters + string.digits
Digits = string.digits
Alphabet = string.ascii_letters

password_length = int(input("Enter length of Password :"))
print("Are you want the password only be in digits with specified length (YES/NO):")
answer = input()

if (answer == "YES"):
    password = ''.join(secrets.choice(Digits) for _ in range(password_length))
    print(f"Secure password generated: {password}")


print("Are you want the password only be in alphabet with specified length (YES/NO):")
answer1 = input()

if (answer1 == "YES"):
    password = ''.join(secrets.choice(Alphabet) for _ in range(password_length))
    print(f"Secure password generated: {password}")

print("Are you want the password should be in digits and alphabets with specified length (YES/NO):")
answer2 = input()

if (answer2 == "YES"):
    password = ''.join(secrets.choice(alphabet) for _ in range(password_length))
    print(f"Secure password generated: {password}")
