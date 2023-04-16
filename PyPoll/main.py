import os
import csv

# Set path to data file
vote_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Set variables
votes = []
Charles_count = 0
Diana_count = 0
Raymon_count = 0

# Defines function to turn csv into list
def make_list(election_data):
    
    name = str(election_data[2])
    votes.append(name)

    # Counts up votes
    if name == "Charles Casper Stockham":

        global Charles_count
        Charles_count = Charles_count + 1

    if name == "Diana DeGette":

        global Diana_count
        Diana_count = Diana_count + 1

    if name == "Raymon Anthony Doane":

        global Raymon_count
        Raymon_count = Raymon_count + 1


# Read in the CSV file
with open(vote_csv, 'r') as csvfile:

    # Split the data on commas and skip header
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    # Makes date and profit lists
    for row in csvreader:
        make_list(row) 

# Variable to clean up
Total_vote_count = Raymon_count + Diana_count + Charles_count
Charles_percent = round(Charles_count / Total_vote_count * 100, 3)
Diana_percent = round(Diana_count / Total_vote_count * 100, 3)
Raymon_percent = round(Raymon_count / Total_vote_count * 100, 3)
winning_vote = max(Charles_count, Diana_count, Raymon_count)
winner = ""

# Sets winner
if winning_vote == Charles_count:

    winner = "Charles Casper Stockham"

if winning_vote == Diana_count:

    winner = "Diana DeGette"

if winning_vote == Raymon_count:

    winner == "Raymon Anthony Doane"

#Prints out results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {Total_vote_count}")
print("--------------------------")
print(f"Charles Casper Stockham: {Charles_percent}% ({Charles_count})")
print(f"Diana DeGette: {Diana_percent}% ({Diana_count})")
print(f"Raymon Anthony Doane: {Raymon_percent}% ({Raymon_count})") 
print("--------------------------")
print(F"Winner: {winner}")
print("--------------------------")

# Set path to file
output_file = os.path.join('PyPoll', 'analysis', 'Results.txt')

# Open the file
with open(output_file, "w") as textfile:

    # Write the header row
    textfile.write("Financial Analysis\n")
    textfile.write("Election Results\n")
    textfile.write("--------------------------\n")
    textfile.write(f"Total Votes: {Total_vote_count}\n")
    textfile.write("--------------------------\n")
    textfile.write(f"Charles Casper Stockham: {Charles_percent}% ({Charles_count})\n")
    textfile.write(f"Diana DeGette: {Diana_percent}% ({Diana_count})\n")
    textfile.write(f"Raymon Anthony Doane: {Raymon_percent}% ({Raymon_count})\n") 
    textfile.write("--------------------------\n")
    textfile.write(F"Winner: {winner}\n")
    textfile.write("--------------------------\n")