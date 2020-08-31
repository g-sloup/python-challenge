import os
import csv

num_months = 0
sum_PL = float(0)
total_PL = []
delta_PL = []

monthlyChange = []
budget_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    previous_row = next(csv_file).split(",")

    num_months += 1

    for row in csv_reader:
        num_months += 1
        total_PL.append(int(row[1]))
        delta_PL.append(int(row[1]) - int(previous_row[1]))
        sum_PL = sum_PL + (int(row[1]) - int(previous_row[1]))
        previous_row = row


average = (round(sum_PL / (num_months - 1), 2),


print("Financial Analysis")
print("____________________________________")
print("Total Months:" + str(num_months))
print("Total: $" + str(sum(total_PL))
print("Average Change: " + str(average))


