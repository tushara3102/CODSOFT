import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length_str = input("Specify the number of characters desired in the password: ")
    
    if length_str.isdigit():
        length = int(length_str)
        if length > 0:
            password = generate_password(length)
            print("Generated Password is:", password)
        else:
            print("Password length must be a +ve integer.")
    else:
        print("Invalid input. Please enter a valid +ve integer.")

if __name__ == "__main__":
    main()
