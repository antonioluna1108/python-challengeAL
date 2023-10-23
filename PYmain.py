# Import csv and os operations
import os
import csv

# setup for csv file.
csv_file = "election_data.csv"

# Variables to place data
total_votes = 0
max_votes = 0
candidates = {}
winner = 0
winner_name = ""

# Read CSV file
with open("Resources/election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile)

    # No need for header row
    next(csvreader)

    # Loop through each row in the Csv File
    for row in csvreader: 

        # Count Total Votes
        total_votes += 1

        # Retrieve Candidates Name from rows
        candidate_name = row[2]

        # See if candidate is in candidate dictionary
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            # If not in candidate dictionary, add them
            candidates[candidate_name] = 1

# Calculate results
# Add a new variable to store results
results = []

# Calculate votes into percentages (%)
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))

    if int(votes) > winner: 
        winner = int(votes)
        winner_name = candidate


with open("analysis/PYtollAL.txt","w") as file:


    # Who is the winner?
    # Find candidate with the most votes
    for candidate, votes, percentage in results:
        if votes > max_votes:
            winner = candidate

    # Print Results
    

    stats = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(stats)

    file.write(stats)

    for candidate, votes, percentage in results:
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    stats = (
        f"-------------------------\n"
        f"Winner: {winner_name}\n"
        f"-------------------------\n")
    print(stats)
    file.write(stats)