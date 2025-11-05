# Rainfall data analyzer

months_counted = 0
cumulative_inches = 0.0

duration_years = int(input("Specify how many years of rainfall data to input:\n"))

year = 0
while year < duration_years:
    print(f"\nRecording data for Year {year + 1}")
    month = 0
    while month < 12:
        rainfall_input = float(input(f"Month {month + 1} rainfall (in inches):\n"))
        cumulative_inches += rainfall_input
        months_counted += 1
        month += 1
    year += 1

monthly_average = cumulative_inches / months_counted

print("\nRainfall Summary")
print(f"Total months: {months_counted}")
print(f"Rainfall accumulated: {cumulative_inches:.2f} inches")
print(f"Average rainfall per month: {monthly_average:.2f} inches")
