import string

def check_password_strength():
    password = input("Enter password : ")
    counts = {
        'lower': sum(c in string.ascii_lowercase for c in password),
        'upper': sum(c in string.ascii_uppercase for c in password),
        'digit': sum(c in string.digits for c in password),
        'space': sum(c == ' ' for c in password),
        'special': sum(c not in string.printable for c in password)
    }

    strength = len([t for t in counts.values() if t])  # Count non-zero categories
    remarks = ('Very Weak', 'Weak', 'Moderate', 'Strong', 'Very Strong')[strength - 1]

    print("Password has : ")
    for kind, count in counts.items():
        print(f'{count} {kind} letters')  

    print(f'Password Score : {strength * 20}/ 100')  
    print('Password Strength : ' + remarks)

def check_another_password():
    while True:
        if input("Check another password? (y/n): ").lower() not in ['y', 'yes']:
            print("Goodbye!")
            return False
        return True

if __name__ == '__main__':
    while True:
        check_password_strength()
        if not check_another_password():
            break
