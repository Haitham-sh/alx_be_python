def safe_divide(numerator, denominator):
    try:
        return f"The result of the division is {float(numerator) / float(denominator)}"
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    except ValueError:
        raise ValueError("Error: Please enter numeric values only.")