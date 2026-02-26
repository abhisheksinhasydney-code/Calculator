"""Command-line interface for the Python calculator."""

from calculator.operations import add, divide, multiply, subtract
from calculator.utils import get_number_input, get_operation_choice, should_continue


def run_calculator() -> None:
    """Run the calculator menu loop until the user exits."""
    while True:
        print("\n=== Python Calculator ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = get_operation_choice()

        if choice == "5":
            print("Goodbye!")
            break

        first_number = get_number_input("Enter the first number: ")
        second_number = get_number_input("Enter the second number: ")

        try:
            result = perform_operation(choice, first_number, second_number)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

        if not should_continue():
            print("Goodbye!")
            break


def perform_operation(choice: str, first_number: float, second_number: float) -> float:
    """Dispatch the selected operation and return the result."""
    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide,
    }
    return operations[choice](first_number, second_number)


if __name__ == "__main__":
    run_calculator()
