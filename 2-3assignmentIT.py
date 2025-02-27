import datetime

def main():
    """Prompts the user for their name and age, then prints a greeting message."""

    # Get the user's name
    name = input("What is your name? ")

    # Get the user's age (as a string)
    age_str = input("How old are you? ")

    # Convert the user's age to an integer
    try:
        age = int(age_str)
    except ValueError:
        print("Invalid age. Please enter a number.")
        return

    # Calculate the year the user was born
    current_year = datetime.datetime.now().year
    year_born = current_year - age

    # Print a greeting message
    print(f"Hello {name}! You were born in {year_born}.")

if __name__ == "__main__":
    main()
