"""Input validation and utility helpers for the calculator CLI."""


def get_number_input(prompt: str) -> float:
    """Prompt for a number until a valid float is entered."""
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation_choice() -> str:
    """Prompt for a valid operation menu choice."""
    valid_choices = {"1", "2", "3", "4", "5"}
    while True:
        choice = input("Choose an option (1-5): ").strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please select a number from 1 to 5.")


def should_continue() -> bool:
    """Ask the user whether to continue using the calculator."""
    while True:
        answer = input("Do you want to perform another operation? (y/n): ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Invalid input. Please enter 'y' or 'n'.")
