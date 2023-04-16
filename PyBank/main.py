import os
import csv

# Set path to data file
bank_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Set variables
dates = []
profits = []
profit_changes = []
profit1 = 1088983
profit2 = 0

# Function that returns average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

# Defines function to turn csv into two lists
def make_lists(budget_data):
    date = str(budget_data[0])
    profit = int(budget_data[1])
    
    dates.append(date)
    profits.append(profit)
            
# Read in the CSV file
with open(bank_csv, 'r') as csvfile:

    # Split the data on commas and skip header
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    # Makes date and profit lists
    for row in csvreader:
        make_lists(row)               

    # Calculations with lists
    for X in profits:
            
        profit2 = X
        
        profit_change = profit2 - profit1
        profit1 = profit2
        profit_changes.append(profit_change)

        Total_Profits = (sum(profits))
        Total_Months = (len(dates))

    # Create variables to look cleaner in print and fix list for avg
    Max_change = max(profit_changes)
    Max_date = dates[profit_changes.index(Max_change)]
    Min_change = min(profit_changes)
    Min_date = dates[profit_changes.index(Min_change)]
    profit_changes.remove(0)
    Avg_change = round(average(profit_changes), 2)

    # Print out final data analysis    
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {Total_Months}")
    print(f"Total Profits: ${Total_Profits}")
    print(f"Average Change: ${Avg_change}")
    print(f"Greatest Increase in Profits: {Max_date} (${Max_change})")    
    print(f"Greatest Decrease in Profits: {Min_date} (${Min_change})")
    
# Set path to file
output_file = os.path.join('PyBank', 'analysis', 'Results.txt')

# Open the file
with open(output_file, "w") as textfile:

    # Write the header row
    textfile.write("Financial Analysis\n")
    textfile.write("-----------------------------\n")
    textfile.write(f"Total Months: {Total_Months}\n")
    textfile.write(f"Total Profits: ${Total_Profits}\n")
    textfile.write(f"Average Change: ${round(average(profit_changes), 2)}\n")
    textfile.write(f"Greatest Increase in Profits: {Max_date} (${Max_change}\n)")   
    textfile.write(f"Greatest Decrease in Profits: {Min_date} (${Min_change})\n")


