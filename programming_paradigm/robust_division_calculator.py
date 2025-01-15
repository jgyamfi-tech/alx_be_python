# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division with error handling."""
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."

        # Perform division
        result = num / denom
        return f"The result of the division is {result:.2f}"
    except ValueError:
        return "Error: Please enter numeric values only."
