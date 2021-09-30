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


    for row in reader:
        vote = str(row[0])
        votes.append(vote)

        county = str(row[1])
        counties.append(county)

        candidate = str(row[2])
        candidates.append(candidates)

    total_votes = int(len(votes))
    print(total_votes)

    print(str(len(votes)) + ' Votes')
    print(str(len(counties)) + " Counties")
    print(str(len(candidates)) + " Candidates")


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

           
    
    print(len(khan))
    print(len(correy))
    print(len(li))
    print(len(otooley))
