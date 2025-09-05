import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    chars = ''
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return "Error: No character sets selected."

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def password_strength(password):
    length = len(password)
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Moderate"
    else:
        return "Weak"

while True:
    print("\n--- Password Generator ---")
    try:
        length = int(input("Enter password length: "))
        upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        digits = input("Include digits? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'

        pwd = generate_password(length, upper, lower, digits, symbols)
        print(f"\nGenerated Password: {pwd}")
        print(f"Strength: {password_strength(pwd)}")
    except ValueError:
        print("Error: Please enter a valid number.")

    again = input("\nGenerate another? (y/n): ").lower()
    if again != 'y':
        break
