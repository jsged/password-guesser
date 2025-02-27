# Password Guesser - @jsged 2025

import itertools

def get_combinations(format_string):
    # Define possible characters
    digit_chars = "0123456789"
    letter_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Create a list of possible character sets for each position
    char_sets = [digit_chars if char == 'X' else letter_chars if char == '-' else [char] for char in format_string]

    # Generate all combinations
    return (''.join(combo) for combo in itertools.product(*char_sets))

def main():
    # Get format from user
    format_string = input("Enter password format (use 'X' for digits and '-' for letters): ")

    # Generate all possible passwords
    combinations = get_combinations(format_string)

    # Write to a file
    with open("password_combinations.txt", "w") as file:
        for password in combinations:
            file.write(password + "\n")

    print("All possible combinations have been written to password_combinations.txt")

if __name__ == "__main__":
    main()
