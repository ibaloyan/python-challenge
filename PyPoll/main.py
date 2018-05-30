# main.py  Python Challenge - PyPoll    Author: Inna Baloyan

# For creating file paths across operation system
import os

# For reading CSV file
import csv

# For sorting input CSV file.
import operator

# For cutting out the header
import itertools

# For redirect the standard output to the output file
import sys

###election_data_file = "election_data_1.csv"
election_data_file = "election_data_2.csv"
sorted_election_data_file = "sorted_election_data.csv"
###output_election_data_file = "output_election_data_1.txt"
output_election_data_file = "output_election_data_2.txt"

# Path to collect data from the Resources folder
election_data_CSV = os.path.join('Resources', election_data_file)

# Path to put sorted data from the Resources folder
sorted_el_data_CSV = os.path.join('Resources', sorted_election_data_file)

# Set Total Vote Counter variable
TOTAL_VOTE_COUNT = 0

# Set Vote Counter variable
VOTE_COUNTER = 0

# Set Winner Count variable
WINNER_COUNT = 0

# Set WINNER CANDIDATAE
WINNER_CANDIDATE = "NONE"

# Set Current_Candidate variable
CURRENT_CANDIDATE = "NONE"

# Set Percent of Votes variable
PERCENT_OF_VOTES = 0

# Lists to store output Election Results data for changing number of candidates
Candidate_Name = []
Percent_of_Votes = []
Votes = []

# Read in the election_data_CSV file without header, i.e the first line
with open(election_data_CSV, 'r') as election_data:
      
      # Output all lines to Resources/sorted_el_data_CSV
      sorted_el_data_CSV = itertools.islice(election_data, 1, None) ### skip 1 line, the header

      # Read in the election data file 
      # Voter ID, County, Candidate
      # row{0], row[1], row[2] 
      my_reader = csv.reader(sorted_el_data_CSV, delimiter=',')

      # then sort sorted_el_data_CSV and use it for all program logic
      sorted_csvfile = sorted(my_reader, key=operator.itemgetter(2))
     
      # Loop through all sorted_csvfile
      for row in sorted_csvfile:
      
            # Get Candidate's name
            CANDIDATE = row[2]
            ###print(CANDIDATE)

            # Populate Candidates dictionary with new Candidate, his/her vote counter, percent votes 0% for now
            # If we get to the new candidate, otherwise, encrease count number for previous cadidate
            # Note. That we have to find this previous candidate first.
            if (CANDIDATE != CURRENT_CANDIDATE):
                    
                if CURRENT_CANDIDATE != "NONE":    # not the first time, but candidate changed
           
                    # Add-Record Candidate Name to Candidate_Name[] list
                    Candidate_Name.append(CURRENT_CANDIDATE)

                     # Add-Record Percent of Votes to Percent_of_Votes[] list
                    Percent_of_Votes.append(PERCENT_OF_VOTES)

                    # Add-Record Votes to Votes[] list
                    Votes.append(VOTE_COUNTER)

                    if VOTE_COUNTER > WINNER_COUNT:
                        WNINNER_COUNT = VOTE_COUNTER
                        WINNER_CANDIDATE = CURRENT_CANDIDATE
                    
                    # Reset vote counter for the new candiddate
                    VOTE_COUNTER = 0

            # Now we are working with this candidate
            CURRENT_CANDIDATE = CANDIDATE
               
            # Encrease VOTE_COUNTER for CANDIDATE
            VOTE_COUNTER = VOTE_COUNTER + 1

            # Always encrease the TOTAL_VOTE_COUNT
            TOTAL_VOTE_COUNT = TOTAL_VOTE_COUNT + 1

      # for last candidate of the input file
          
      # Add-Record Candidate Name to Candidate_Name[] list
      Candidate_Name.append(CURRENT_CANDIDATE)
      LIST_LENGTH = len(Candidate_Name)
   
      # Add-Record Percent of Votes to Percent_of_Votes[] list
      Percent_of_Votes.append(PERCENT_OF_VOTES)

      # Add-Record Votes to Votes[] list
      Votes.append(VOTE_COUNTER)

      # Find out what candidate is the WINNER
      if VOTE_COUNTER > WINNER_COUNT:
            WNINNER_COUNT = VOTE_COUNTER
            WINNER_CANDIDATE = CURRENT_CANDIDATE
      
      # Output results to terminal and to the output file
      print("")
      print("```")
      print("Election Results")
      print("-------------------------")
      print("Total Votes: ", TOTAL_VOTE_COUNT)
      print("-------------------------")
    
      # Print out Candidate results here
      ###########################################

      # Calculate Percent of Votes for all Candidates
      for index in range(LIST_LENGTH):
        # Determine Percent of Votes to 2 decimal places  
        Percent_of_Votes[index] = round((Votes[index]/TOTAL_VOTE_COUNT)*100, 2)
        
        # Output election results for each candidate
        print(Candidate_Name[index] + ": " + str(Percent_of_Votes[index]) + "% (" + str(Votes[index]) + ")") 
      ###########################################

      print("-------------------------") 
      print( "Winner: ", WINNER_CANDIDATE)
      print("-------------------------")
      print("```")

      # Redirect all my standard output results ( terminal ) to the output file for historical purposes

      orig_stdout = sys.stdout
      with open(output_election_data_file, "w") as election_output:
        sys.stdout = election_output

         # Output results to terminal and to the output file
        print("")
        print("```")
        print("Election Results")
        print("-------------------------")
        print("Total Votes: ", TOTAL_VOTE_COUNT)
        print("-------------------------")
    
        # Print out Candidate results here
        ########################################################

        # Calculate Percent of Votes for all Candidates
        for index in range(LIST_LENGTH):
            # Determine Percent of Votes to 2 decimal places  
            Percent_of_Votes[index] = round((Votes[index]/TOTAL_VOTE_COUNT)*100, 2)
            # Output election results for each candidate
            print(Candidate_Name[index] + ": " + str(Percent_of_Votes[index]) + "% (" + str(Votes[index]) + ")") 
        ###########################################

        print("-------------------------") 
        print( "Winner: ", WINNER_CANDIDATE)
        print("-------------------------")
        print("```")
        ########################################################

        sys.stdout = orig_stdout
        election_output.close() 

##### The End ###################################################### 