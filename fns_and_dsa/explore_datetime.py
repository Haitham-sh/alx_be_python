from datetime import datetime, timedelta

def display_current_datetime():
    current_datetime = datetime.now()
    print("Current date and time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()

added_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(added_days):
    future_date = datetime.now() + timedelta(days=added_days)
    return future_date.strftime("%Y-%m-%d")

print("Future date:", calculate_future_date(added_days))