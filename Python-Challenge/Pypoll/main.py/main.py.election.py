# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

path = "C:\\Users\\nobin\\Desktop\\Python-Challenge\\Pypoll\\Resources"


csvpath = os.path.join('..', 'Resources', "election_data.csv")

# set variables
total_votes = 0
khan_votes = 0
correy_votes = 0
otooley_votes = 0

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
       
        # count the voter ID's and store in variable total_votes
        total_votes +=1
        
        if row[2] == "Khan":
            Khan_votes +=1
    elif row[2] == "correy":
        correy_votes +=1
elif row[2] == "Li":
    Li_votes +=1
elif row[2] == "O'Tooley":
    otooley_votes +=1
      
      # dictionary list of candidates
    candidates = ["Khan","Correy","Li","O'Tooley",]
    votes = [Khan_votes, correy_votes, otooley_votes]
        
        # using max function of the dictionary
    dict_candidates_and_votes = dict(zip(candidates,votes))
    key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)
    
    
    #print the summary of the analysis
    Khan_percent = (Khan_votes/total_votes)*100
    correy_percent = (correy_votes/total_votes)*100
    li_percent = (li_votes/total_votes)*100
    otooley_percent = (otooley_votes/total_votes)*100
    
    #print the summary table
    print(f"election results")
    print(f"-----------------------")
    print(f"total votes:{total_votes}")
    print(f"-----------------------")
    print(f"Khan: {Khan_percent:.3f}% ({correy_votes})")
    print(f"Li:{li_percent:.3f}% ({li_votes})")
    print(f"o'Tooley: {otooley_percent:,3f} ({otooley_votes})%")
    print(f"------------------------")
    print(f"winner: {key}")
    print(f"------------------------")
    
    
    
        