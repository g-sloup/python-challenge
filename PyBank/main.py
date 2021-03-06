import os
import csv

num_months = 0

sum_Delta = float(0)

total_PL = []
delta_PL = []
months = []

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    previous_row = next(csv_file).split(",")
    num_months += 1
    total_PL.append(int(previous_row[1]))

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
        if item[1] < minimum[1]:
            minimum = item

    return minimum


incr = max_pl(ziplist)
decr = min_pl(ziplist)

print("Financial Analysis")
print("____________________________________")

print("Total Months: " + str(num_months))

print("Total: " + str(sum(total_PL)))

average = sum_Delta / (num_months - 1)
print("Average Change: " + str(round(average, 2)))

print("Greatest Increase in Profits: " + str(incr[0]) + " ($" + str(incr[1]) + ")")
print("Greatest Decrease in Profits: " + str(decr[0]) + " ($" + str(decr[1]) + ")")


output_file = os.path.join("Analysis", "analysis.txt")
with open(output_file, "w") as txt_file:

    txt_file.write("Financial Analysis")

    txt_file.write("____________________________________")

    txt_file.write("Total Months: " + str(num_months))

    txt_file.write("Total: " + str(sum(total_PL)))

    txt_file.write("Average Change: " + str(round(average, 2)))

    txt_file.write("Greatest Increase in Profits: " + str(incr[0]) + " ($" + str(incr[1]) + ")")

    txt_file.write("Greatest Decrease in Profits: " + str(decr[0]) + " ($" + str(decr[1]) + ")")
