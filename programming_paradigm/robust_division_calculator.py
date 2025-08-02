def safe_divide(numerator, denominator):
    try:
        return f"The result of the division is {float(numerator) / float(denominator)}"
    except ZeroDivisionError:
        print ("Cannot divide by zero.")
    except ValueError:
        print ("Please enter numeric values only.")