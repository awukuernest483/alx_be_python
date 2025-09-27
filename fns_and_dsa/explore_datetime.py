from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    format_str = "%Y-%m-%d %H:%M:%S"
    print("Current date and time:", current_date.strftime(format_str))

display_current_datetime()

number_of_days = int(input("Enter number of days to add: "))
def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))
    

calculate_future_date(number_of_days)
