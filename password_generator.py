import random
import string

def random_char(char_set):
    return random.choice(char_set)

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c in string.ascii_uppercase for c in password):
        score += 1
    if any(c in string.ascii_lowercase for c in password):
        score += 1
    if any(c in string.digits for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if score <= 2:
        return "WEAK"
    elif score <= 3:
        return "MEDIUM"
    elif score <= 4:
        return "STRONG"
    else:
        return "VERY STRONG"

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    char_pool = ""
    guaranteed = []
    if use_upper:
        char_pool += string.ascii_uppercase
        guaranteed.append(random_char(string.ascii_uppercase))
    if use_lower:
        char_pool += string.ascii_lowercase
        guaranteed.append(random_char(string.ascii_lowercase))
    if use_digits:
        char_pool += string.digits
        guaranteed.append(random_char(string.digits))
    if use_symbols:
        char_pool += string.punctuation
        guaranteed.append(random_char(string.punctuation))
    if not char_pool:
        raise ValueError("At least one character type must be selected.")
    remaining = [random_char(char_pool) for _ in range(length - len(guaranteed))]
    password_list = guaranteed + remaining
    random.shuffle(password_list)
    return "".join(password_list)

while True:
    print("")
    print("*** Password Generator ***")
    count = int(input("How many passwords do you want?: "))
    length = int(input("Enter password length: "))
    upper = input("Include uppercase? (yes/no): ")
    use_upper = upper.lower() == "yes"
    lower = input("Include lowercase? (yes/no): ")
    use_lower = lower.lower() == "yes"
    digits = input("Include digits? (yes/no): ")
    use_digits = digits.lower() == "yes"
    symbols = input("Include symbols? (yes/no): ")
    use_symbols = symbols.lower() == "yes"
    print("")
    for i in range(count):
        pwd = generate_password(
            length=length,
            use_upper=use_upper,
            use_lower=use_lower,
            use_digits=use_digits,
            use_symbols=use_symbols)
        strength = check_strength(pwd)
        print("Password", i+1, ":", pwd, "→", strength)
    print("")
    again = input("Generate again? (yes/no): ")
    if again.lower() == "no":
        print("GOODBYE!! Have a nice day!")
        break
    
0

