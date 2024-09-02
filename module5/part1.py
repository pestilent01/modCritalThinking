'''
Part1 :
Write a program that uses nested loops to collect data and calculate the 
average rainfall over a period of years. The program should first ask for 
the number of years. The outer loop will iterate once for each year. 
The inner loop will iterate twelve times, once for each month. Each 
iteration of the inner loop will ask the user for the inches of rainfall 
for that month. After all iterations, the program should display the number of 
months, the total inches of rainfall, and the average rainfall per month for 
the entire period.
'''

numYears = int(input("Enter the number of years: \n"))
totalMonths = 0
totalRainfall = 0.0
for year in range(1,numYears+1):
    print(f'Enter the rainfall for each month for the year {year}')
    for month in range(1,13):
        monthRainFall = float(input(f"Rainfall(inches) for month {month}: \n"))
        totalRainfall += monthRainFall
        totalMonths += 1

print(f'Total Months: {totalMonths}')
print(f'Total Rainfal(in inches): {totalRainfall:.2f}')
print(f'Average Rainfall(in inches) per Month: {totalRainfall/totalMonths:.2f}')