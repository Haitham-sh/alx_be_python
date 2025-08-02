def safe_divide(numerator, denominator):
    try:
        return f"The result of the division is {float(numerator) / float(denominator)}"
    except ZeroDivisionError:
        raise ("Error: Cannot divide by zero.")
    except ValueError:
        raise ("Error: Please enter numeric values only.")