# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:
     # CSV reader specifies delimiter and variable that holds contents ls
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Initialize variables
    total_votes = 0
    candidate_votes = {}
    candidates = []

    # Loop through each row in the CSV file
    for row in csvreader:
        # Skip the header row
        if row[0] == 'Ballot ID':
            continue

        # Count the total number of votes
        total_votes += 1

        # Add candidate to list if not already in list
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1

    # Calculate the percentage of votes each candidate won
    percentages = {}
    for candidate in candidates:
        percent = round(candidate_votes[candidate] / total_votes * 100, 2)
        percentages[candidate] = percent

    # Find the winner of the election
    winner = max(candidate_votes, key=candidate_votes.get)

    # Print the results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate in candidates:
        print(f"{candidate}: {percentages[candidate]}% ({candidate_votes[candidate]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    with open("Analysis/Pypoll.txt", 'w') as file_PythonChallenge:
        file_PythonChallenge.write(f"Election Results \n")
        file_PythonChallenge.write('-------------------------------------\n')
        file_PythonChallenge.write(f'Total Votes: {total_votes}\n')
        for candidate in candidates:
            file_PythonChallenge.write(f'{candidate}: {percentages[candidate]}% ({candidate_votes[candidate]})\n')
        file_PythonChallenge.write(f'Winner: {winner}\n')
        file_PythonChallenge.write('-----------------------------------\n')



                          




