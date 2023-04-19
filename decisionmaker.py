import random

MAX_DECISIONS = 10

def get_number_of_decisions():
    while True:
        try:
            amount_input = input(f"How many choices are there in total? \nEnter a number from 1 - {MAX_DECISIONS}: ")
            amount = int(amount_input)  # Convert input to an integer
            if MAX_DECISIONS >= amount > 0:  # Check if input is within the valid range
                break
            elif amount <= 0:
                print("Please enter a positive number.")
            else:
                print(f"Please enter a number from 1 - {MAX_DECISIONS}")
        except ValueError:
            # Handle non-integer input
            print("Enter a valid number of choices")
    return amount


def get_decisions(count):
    choices = []
    for i in range(count):
        choice_input = input(f"Great! Enter choice number {i + 1}: ")
        choices.append(choice_input)  # Add choices to the list
    return choices


def randomize_choices(choices):
    return random.choice(choices)  # Randomly select a choice from the list


def main():
    while True:
        print("Welcome to the Decision Maker")
        quit_option = input(
            "Are you ready to go? (Press 'q' to quit or any other key to continue): ")
        if quit_option.lower() == "q":
            break

        count = get_number_of_decisions()
        choices = get_decisions(count)
        print(randomize_choices(choices))  # Print randomly selected choice

        while True:
            yes_or_no = input(
                "Refresh? Press Enter to refresh (Press 'q' to quit): ")
            if yes_or_no.lower() == "q":
                break
            else:
                # Print randomly selected choice
                print(randomize_choices(choices))


main()
