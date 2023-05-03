# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    total_months = 0
    profit_loss = 0
    change = []
    previous_pl = 0
    max_increase = 0
    max_decrease = 0
    max_increase_date = ''
    max_decrease_date = ''
    csvlist = []

    for row in csvreader:
        #print('month: ' + row[0])
       # print('p&l:   ' + row[1])
        profit_loss = profit_loss + int(row[1])
        if (total_months > 0):
            change.append(int(row[1]) - previous_pl)
        previous_pl = int(row[1])
        total_months = total_months + 1
        csvlist.append(row)

        
            
   #calculate average change in profit 
    ch=0
    for n in range(len(change)):
        ch+= change[n]
  
#calculate greatest increase in profit and greatest decrease in profit  
        if change[n] > max_increase:
                max_increase = change[n]
                max_increase_date = csvlist[n+1][0]
                
        if change[n] < max_decrease:
                max_decrease = change[n]
                max_decrease_date = csvlist[n+1][0]

    avg_change = ch / len(change)

 


print ("Financial Analysis")
print ("----------------------------------")
print(total_months)
print(profit_loss)
print(change)
print(len(change))
print(avg_change)
print(f"greatest increase in profits:{max_increase_date} (${max_increase})")
print(f"greatest decrease in profits:{max_decrease_date} (${max_decrease})")

with open("Analysis/Pybank.txt", 'w') as file_PythonChallenge:
     file_PythonChallenge.write(f"""Financial Analysis
----------------------------------
total_months: {total_months}
total: {profit_loss}
avg_change: {round(avg_change,2)}
greatest increase in profit:  {max_increase_date}  (${max_increase})
greatest decrease in profits: {max_decrease_date}  (${max_decrease})
     """)


