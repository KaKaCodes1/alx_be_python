from datetime import datetime, timedelta

def display_current_datetime():
    return datetime.now()

def calculate_future_date(no_of_days):
    current_date = datetime.now()
    return current_date + timedelta(days=no_of_days)

current_date = display_current_datetime()
print("Current date and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))

no_of_days = int(input("Enter the number of days to add to the current date: "))
future_date = calculate_future_date(no_of_days)
print("Future date: ", future_date.strftime("%Y-%m-%d"))
