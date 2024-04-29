import random
import string
import sys
import argparse

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def main():
    parser = argparse.ArgumentParser(description="Generate a random password of specified length")
    parser.add_argument("length", type=int, help="Length of the password")
    args = parser.parse_args()
    if args.length <= 0 or type(args.length) != int:
            print("Error: Length must be a positive integer")
            return

    password = generate_password(args.length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
