"""Streamlit web interface for the Python calculator."""

from typing import Callable, Dict

import streamlit as st

from calculator.operations import add, divide, multiply, subtract

OperationFunction = Callable[[float, float], float]


def get_operation_map() -> Dict[str, OperationFunction]:
    """Return a mapping of operation labels to operation functions."""
    return {
        "Add": add,
        "Subtract": subtract,
        "Multiply": multiply,
        "Divide": divide,
    }


def calculate_result(first_number: float, second_number: float, operation_label: str) -> float:
    """Calculate and return the operation result for the selected label."""
    operations = get_operation_map()
    operation = operations[operation_label]
    return operation(first_number, second_number)


def render_app() -> None:
    """Render the Streamlit calculator UI."""
    st.set_page_config(page_title="Python Calculator", page_icon="+", layout="centered")

    st.title("Python Calculator")
    st.write("Enter two numbers, choose an operation, and click **Calculate**.")

    first_number = st.number_input("First number", value=0.0, format="%0.6f")
    second_number = st.number_input("Second number", value=0.0, format="%0.6f")

    operation_label = st.selectbox(
        "Operation",
        options=list(get_operation_map().keys()),
        index=0,
    )

    if st.button("Calculate", type="primary"):
        try:
            result = calculate_result(first_number, second_number, operation_label)
            st.success(f"Result: {result}")
        except ZeroDivisionError:
            st.error("Division by zero is not allowed. Please enter a non-zero second number.")


if __name__ == "__main__":
    render_app()
