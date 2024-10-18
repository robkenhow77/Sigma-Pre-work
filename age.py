import datetime

print("Input date of birth (day, month, year)")
birthday = [int(x) for x in input().split(", ")]
date = datetime.datetime.now()
year_difference = date.year - birthday[2]
month_difference = date.month - birthday[1]
print(f'You are {year_difference} years and {month_difference} months old')
