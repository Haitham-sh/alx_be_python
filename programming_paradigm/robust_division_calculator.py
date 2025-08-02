def safe_divide(numerator, denominator):
    try:
        return float((numerator / denominator),1)
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    except ValueError:
        raise ValueError("Error: Please enter numeric values only.")