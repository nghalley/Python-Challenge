# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

path = "C:\\Users\\nobin\\Desktop\\Python-Challenge\\PyBank\\Resources"


#set variables 
csvpath = os.path.join(path, "budget_data.csv")
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        first_row = next(csvreader)
                    
        total_pl += int(first_row[1])
        value = int(first_row[1])        
    
    for row in csvreader:
        dates.append(row[0])
        
        change = int(row[1]).value
        profit.append(change)
        value = int(row[1])
        
        total_months += 1
         
         #Total net amount of "profit/losses over entire period"
        total_pl = total_pl + int(row[1])
        
        greatest_increase = max(profits)
        greatest_index = profits.index(greatest_increase)
        greatest_date = dates[greatest_index]
        
        
        greatest_decrease = min(profit)
        worst_index = profits.index(greatest_decrease)
        worst_date = dates(worst_index)
        
        #average change in "profit/losses between months overs entire period"
        avg_change = sum(profits)/len(profits)
        
        
    print("Financial Analysis")
    print("--------------------------")
    print(f"totol months: {str(total_months)}")
    print(f"total: ${str(total_pl)}")
    print("Average Change: ${str(round(avg_change,2))")
    print(f"Greatest Increase in profits:{greatest_date}(${str(greatest_increase)})")
    print(f"Greatest Decrease in profits: {worst_date}(${str(greatest_decrease)})")
    #Exporing to .txt file
    output = open("output.txt", "w")
    
    line1 = "Financial Analysis"
    line2 = "---------------------"
    line3 = str("Total Months: {str(total_months)}")
    line4 = str("Total: ${str(total_pl)}")
    line5 = str("Average Change: ${str(round(avg_change,2))}")
    line6 = str("Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
    line7 = str("Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
    output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))  