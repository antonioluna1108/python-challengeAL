#  Start off by importing csv and os operations
import os
import csv


# Variables to place data
total_months = 0 
total_profit = 0
prev_profit_loss= 0
change = 0 
total_change = 0 
change_count = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]

# Read Csv File
with open("Resources/budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # No need for header row
    next(csvreader)

    # Loop through each row in the Csv File
    for row in csvreader: 
        
        # Count Total Months
        total_months += 1
        total_profit += int(row[1])

        # Sum the total profits and losses
        if prev_profit_loss != 0:
            change = int(row[1]) - prev_profit_loss
            total_change += change
            change_count += 1

        # Find change in profits and losses between current and prevoius rows
       
        prev_profit_loss = int(row[1])

        # Find greatest increase of profits for the whole period
        if (change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = change

        # Find greatest loss for the whole period
        if (change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change




# Print analysis for terminal

output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit}
Average Change: ${total_change / change_count:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
"""
# Export Results into txt file
print(output)

with open("analysis/PYBANKAL.txt", "w") as file:
    file.write(output)


