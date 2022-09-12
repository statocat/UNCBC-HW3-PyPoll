# dependencies
import csv
import os

# load data
file_load = os.path.join('Deliverables', 'election_results.csv')

# file to save analysis
file_write = os.path.join('Deliverables','election_results.txt')

# initialize variable to store total number of votes cast in election
total_votes = 0

# inititalize empty list to store names of all candidates that recieved votes
candidate_names = []

# initialize empty dictionary to store number of votes cast for each candidate
candidate_votes = {}

# initialize variables to hold winner name, votes received, and percentage of votes received.
winner = ''
winner_votes = 0
winner_percentage = 0

### Challenge Step 1 ###
#initialize empty list to store names of all counties in which voters are registered
county_names = []

#initialize empty dictionary to store the total number of votes casted in each county
county_votes={}

### Challenge Step 2 ###
# initialize variable to hold county with largest turnout
top_county = ''

# initialize variable to hold the number of votes cast in that county.
top_county_votes=0

# read in data
with open(file_load) as election_data:

    file_reader = csv.reader(election_data)

    # read and print header row
    headers = next(file_reader)

    for row in file_reader:
        # Compute total number of votes cast in election
        total_votes += 1

        # Make a complete list of candidates who received votes
        candidate = row[2]
        
        ### Challenge Step 3 ###
        # Use for loop to get county name from each row
        county = row[1]

        if candidate not in candidate_names:
            candidate_names.append(candidate)
            candidate_votes[candidate]=0
        
        ### Challenge Step 4a-c ### 
        # make list of unique county names and initialize count to zero
        if county not in county_names:
            county_names.append(county)
            county_votes[county]=0
        
        # Tally votes for each candidate
        candidate_votes[candidate]+= 1
        
        ### Challenge Step 5 ###
        # Tally votes for each county
        county_votes[county] += 1

# make summary of election results
election_results = (
    f'\nElection Results\n'
    f'--------------------------\n'
    f'Total Votes: {total_votes:,}\n'
    f'--------------------------\n'
    f'\n'        
)


# Print summary for election, each candidate, and for winner and write to text file
with open(file_write,'w') as txt_file:
    
    print(election_results)
    txt_file.write(election_results)

    print('County Votes:\n')
    txt_file.write('County Votes:\n')

    for county in county_votes:
        ### Challenge Step 6a-d ###
        # build and print summary of turnout in each county
        votes = county_votes[county]
        percentage = 100* float(votes)/float(total_votes)
        print(f'{county}: {percentage:.1f}% ({votes:,})')

        ### Challenge Step 6e ###
        # write summary of results for each county to txt_file
        txt_file.write(f'{county}: {percentage:.1f}% ({votes:,})\n')

        ### Challenge Step 6f ###
        # Determine the county with largest turnout and print summary
        if votes > top_county_votes:
            top_county = county
            top_county_votes =  votes
            top_county_percentage = percentage

    ### Challenge Step 7 ###
    # write a print statement to state county with largest turnout
    top_county_summary =(
        f'\n'
        f'--------------------------\n'
        f'Largest County Turnout: {top_county}\n'
        f'--------------------------\n'
    )
    print(top_county_summary)

    ### Challenge Step 8 ###
    # State the county with largest turnout and write to text file
    txt_file.write(top_county_summary)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        # 4. Compute percentage of vote received by each candidate
        percentage = 100* float(votes)/float(total_votes)
        print(f'{candidate}: {percentage:.1f}% ({votes:,})\n')
        txt_file.write(f'{candidate}: {percentage:.1f}% ({votes:,})\n')

        # 5. Determine winner (one with most votes)
        if votes > winner_votes:
            winner = candidate
            winner_votes =  votes
            winner_percentage = percentage

    winner_summary = (
        f'--------------------------\n'
        f'Winner: {winner}\n'
        f'Winning Vote Count: {winner_votes:,}\n'
        f'Winning Percentage: {winner_percentage:.1f}%\n'
        f'--------------------------\n'
    )

    print(winner_summary)
    txt_file.write(winner_summary)
