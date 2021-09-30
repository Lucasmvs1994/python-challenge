print ('Hey')

#setting modules...

import os
import csv 


# parsing the csv file headers...

filename = "election_data.csv"
print (filename)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

# Printing Headers and Their Positions

    for index, column_header in enumerate(header_row):
        print(index, column_header)


# Extracting, Reading and Counting votes, counties and candidates

    votes = []
    counties = []
    candidates = [] 
    khan = []
    correy = [] 
    li = [] 
    otooley = [] 
    unique_candidates = []

    for row in reader:
        vote = str(row[0])
        votes.append(vote)

        county = str(row[1])
        counties.append(county)

        candidate = str(row[2])
        candidates.append(candidate)

    total_votes = int(len(votes))
    print(total_votes)

    print(str(len(votes)) + ' Votes')
    print(str(len(counties)) + " Counties")
    print(str(len(candidates)) + " Candidates")


# unique candidates...how to get there?? 
    









# analyzing candidates who received votes + votes by person 
    for x in candidates:  
        if x == "Khan":
            khan.append(candidates)
            
        elif x == "Correy":
            correy.append(candidates)

        elif x == "Li":
            li.append(candidates)

        else:
            otooley.append(candidates)

           
    
    print(str(len(khan)) + " votes for Khan...he is the winner")
    print(str(len(correy)) + " votes for Correy...")
    print(str(len(li)) + " votes for Li..." )
    print(str(len(otooley)) + " votes for Otooley...")


# setting votes per candidate... 

    khan_votes = len(khan)
    print(khan_votes)

    correy_votes = len(correy)
    print(correy_votes)

    li_votes = len(li)
    print(li_votes)

    otooley_votes = len(otooley)
    print(otooley_votes)


# calculating percentages 


    khan_percentage = khan_votes / total_votes *100
    print(khan_percentage)

    correy_percentage = correy_votes / total_votes *100 
    print(correy_percentage)

    li_percentage = li_votes / total_votes *100
    print(li_percentage)
    
    otooley_percentage = otooley_votes / total_votes*100
    print(otooley_percentage)

    print(f'The winner of the election is Khan')