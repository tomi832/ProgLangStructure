from datetime import datetime, timedelta

# found the datetime package and the needed functions, a bit advanced but it's using Python's standard library
# to handle date manipulations and be able to concat them into a list comprehension
dates_list_maker = lambda start, length, step: [
    (datetime.strptime(start, "%d-%m-%Y") + timedelta(days=step * i)).strftime("%d-%m-%Y")
    for i in range(length)
]

# example
print(dates_list_maker("25-09-2025", 5, 2))