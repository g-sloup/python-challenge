# * The total number of votes cast
totalVotes = 0

#  * A complete list of candidates who received votes
candidates []

print(candidates)

poll_csv = os.path.join("Resources", "election_data.csv")
with open(poll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# Skip over header line
    csv_header = next(csv_file)

# Skip over first row of data
    previous_row = next(csv_file).split(",")

# Add first row to month count and total
    num_months += 1
    total_PL.append(int(previous_row[1]))
    months.append(str(previous_row[0]))

# Begin For Loop at second row adding 1 to total number of months,
    # adding each profit/loss to total, adding monthly delta to list

    for row in csv_reader:
        num_months += 1
        months.append(row[0])
        total_PL.append(int(row[1]))
        delta_PL.append(int(row[1]) - int(previous_row[1]))
        sum_Delta = sum_Delta + (int(row[1]) - int(previous_row[1]))
        previous_row = row

* The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
print("Election Results")

print("-------------------------")
print("Total Votes: " + str )
print("-------------------------")
print("Khan: " +
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```
