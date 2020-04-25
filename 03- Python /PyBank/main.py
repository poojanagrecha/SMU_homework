import csv
import os
csvpath = r"SMU stuff/smu-dal-data-pt-03-2020-u-c/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"
file_to_output = os.path.join("SMU_homework/03- Python /PyBank", "budget_analysis.txt")

totalMonths = 0
totalProfit = 0
profitChanges = []
lastProfit = 0
currentProfit = 0
rowCount = 0
greatestIncrease = 0 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader: 
        #print(row)
        totalMonths += 1 
         
        totalProfit += int(row[1])
        

        if rowCount == 0:
            lastProfit = int(row[1])
            greatestIncreasemonth = (row[0])
            greatestDecreasemonth = (row[0])
            greatestIncrease = 0
            greatestDecrease = 0
        else:
            currentProfit = int(row[1])
            difference = currentProfit - lastProfit
            profitChanges.append(difference)
            lastProfit = currentProfit
            if greatestIncrease > difference:
                pass
            else: 
                greatestIncrease = difference
                greatestIncreasemonth = (row[0])
            if greatestDecrease < difference:
                pass
            else: 
                greatestDecrease = difference
                greatestDecreasemonth = (row[0])


        
        rowCount += 1 
    print(profitChanges)
    average = sum(profitChanges)/ len(profitChanges)
    greatestIncrease = max(profitChanges)


    print ("Financial Analysis:")
    print("Total Months:" + str(totalMonths))
    print('Total Profit:' + "$" + str(totalProfit))
    print('Average Change:'+ "$" + str(average))
    print('Greatest Increase in Profits ' + str(greatestIncreasemonth) + " " + "$" + str(greatestIncrease))
    print('Greatest Decrease in Profits ' + str(greatestDecreasemonth) + " " + "$" + str(greatestDecrease))


