import os
import csv

# Variable for Total number of months
num_months = 0

# Variable for Monthly PL change
sum_Delta = float(0)

# Create Lists for monthly profit loss and monthly change
total_PL = []
delta_PL = []
months = []


budget_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# Skip over header line
    csv_header = next(csv_file)

# Skip over first row of data
    previous_row = next(csv_file).split(",")

# Add first row to month count and total
    num_months += 1
    total_PL.append(int(previous_row[1]))

# Begin For Loop at second row adding 1 to total number of months,
    # adding each profit/loss to total, adding monthly delta to list

    for row in csv_reader:
        num_months += 1
        months.append(row[0])
        total_PL.append(int(row[1]))
        delta_PL.append(int(row[1]) - int(previous_row[1]))
        sum_Delta = sum_Delta + (int(row[1]) - int(previous_row[1]))
        previous_row = row

ziplist = list(zip(months, delta_PL))


def max_pl(sequence):
    if not sequence:
        raise ValueError('empty sequence')

    maximum = sequence[0]

    for item in sequence:
        if item[1] > maximum[1]:
            maximum = item

    return maximum


def min_pl(sequence):
    if not sequence:
        raise ValueError('empty sequence')

    minimum = sequence[0]

    for item in sequence:
        # Compare elements by their weight stored
        # in their second element.
        if item[1] < minimum[1]:
            minimum = item

    return minimum


incr = max_pl(ziplist)
decr = min_pl(ziplist)

print("Financial Analysis")
print("____________________________________")

# Print Total Months
print("Total Months: " + str(num_months))

# Print Total Profit Loss
print("Total: " + str(sum(total_PL)))

# Print Average Change
average = sum_Delta / (num_months - 1)
print("Average Change: " + str(round(average, 2)))

# Print Greatest Profit Change
print("Greatest Increase in Profits: " + str(incr[0]) + " ($" + str(incr[1]) + ")")
print("Greatest Decrease in Profits: " + str(decr[0]) + " ($" + str(decr[1]) + ")")

# res = [months.index(i) for i in delta_PL)
# Find index of max(delta_PL)

# indexIncr = (delta_PL.index(max(delta_PL)))
# indexDecr = (delta_PL.index(min(delta_PL)))

#    if months.index(i) == delta_PL.index("maxIncr"):
#         maxMonth = months[indexIncr]
#     print("Greatest Increase: " + months[indexIncr] + "(" + delta_PL ")")
# maxMonth = [months.index(i) for i in delta_PL]