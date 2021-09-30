filename = 'note1.txt'

with open(filename, 'w') as file_object:
    file_object.write("1. There are a total of 86 months included in the dataset.\n\n")
    file_object.write("2. The net total amount of Profit/Losses over the entire period is $38,382,578.\n\n")
    file_object.write("3. The average of changes is $-2315.12.\n\n")
    file_object.write("4. Greatest Increase in Profits: Feb-2012 ($1,926,159).\n\n")
    file_object.write("5. Greatest Decrease in Profits: Sep-2013 ($-2,196,167).\n\n")