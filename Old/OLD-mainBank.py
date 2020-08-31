# The average of the changes in "Profit/Losses" over the entire period
    # For Loop, find difference between row[1] + 1 and row[1]
    # Divide by (total number of months - 1)

# The greatest increase in profits (date and amount) over the entire period
    # Find highest number in monthly change list. Print - number

# The greatest decrease in losses (date and amount) over the entire period


# Print the analysis to the terminal and export a text file with the results.

import os
import csv

num_months = []
total_PL = []
monthlyChange = []

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    previous_row = next(csv_file)
    num_months.append((previous_row[0]))
    total_PL.append(int(previous_row[1]))

    # previous_row =

    for row in csv_reader:
        num_months.append(row[0])
        total_PL.append(int(row[1]))
        # Change = int(row[1]) - int(previous_row[1])
        # monthlyChange.append(Change)


print("Total Months: " + str(len(num_months)))
print("Total: $" + str(sum(total_PL)))
# print("Average Change: $" + str(sum(monthlyChange)/(sum(num_months) - 1)))
# print("Greatest Increase in Profits: " + str(
# print(Greatest Decrease in Losses: " + str(


        # Assign as Row 3
        #previous_row = int
    # Running though Row 4 looking back prior to For at Row 2
# AvDivBy = (len(num_months) - 1)

# PL = int(row[1])