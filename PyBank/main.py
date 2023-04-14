import os
import csv

#set path to data file
bank_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#set variables
dates = []
profits = []
profit_changes = []
starting_profit = 0
new_profit = 0

# Define the function and have it accept the 'state_data' as its sole parameter
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

    for row in csvreader:
        make_lists(row)               

        for X in profits:
            
            new_profit = profits(X)

            if new_profit > 0:
                profit_change = starting_profit + new_profit
                starting_profit = new_profit
                profit_changes.append(profit_change)
            else:
                profit_change = starting_profit - new_profit
                starting_profit = new_profit
                profit_changes.append(profit_change)



        Total_Profits = (sum(profits))
        Total_Months = (len(dates))

    #Print out final data analysis    
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {Total_Months}")
    print(f"Total Profits: ${Total_Profits}")
    # print(f"Average Change: ${}")
    # print(f"Greatest Increase in Profits: {} (${})")    
    # print(f"Greatest Decrease in Profits: {} (${})")
    print(profit_change)

#
# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

