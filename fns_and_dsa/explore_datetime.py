from datetime import datetime, timedelta

current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time:", current_date)

added_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(added_days):
    future_date = datetime.now() + timedelta(days=added_days)
    return future_date.strftime("%Y-%m-%d")

print("Future date:", calculate_future_date(added_days))