print ('Hey')

#setting modules...

import os
import csv 



# parsing the csv file headers...

filename = "budget_data.csv"
print (filename)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

# Printing Headers and Their Positions

    for index, column_header in enumerate(header_row):
        print(index, column_header)

# Extracting, Reading and Counting dates 

    #dates = []
    #for row in reader:
       # date = str(row[0])
        #dates.append(date)
   # print(dates)

    #print(str(len(dates)) + ' Months' )

# Extracting, Reading, and Summing Profit/Losses
    totals = []
    for row in reader:
        total = int(row[1])
        totals.append(total)
    #print(totals)
        
    Sum = sum(totals)
    print('The net total amount of Profit/Losses over the entire period is ' + str(Sum))
   #print(len(totals))
    
    
# Calculating the average change...
    change = 671099 - 867884 
    average_of_change = change/len(totals)
    print('The Average change is ' + str(average_of_change))

    #Finding the greatest increase in profits (date and amount) over the entire period
    Max = max(totals)
    print('Greatest Increase in Profits: ' + str(Max))


#Finding the greatest decrease in Profits (date and amount) over the entire period
    Min = min(totals)
    print('Greates Deacrease in Profits: ' + str(Min))










