# Project Brief: Spreadsheet Analysis / Data Analysis
# In this project you'll use Python to do very basic data analysis on a spreadsheet. The standard
# project will use csv file that contains fake sales data. After completing the required tasks you are
# free to change the csv file that you use.
# The csv file for the standard project is called sales.csv and is included with your course materials.

#  1. Read the data from the spreadsheet

# import csv and math libraries
import csv
import math

file = open("sales.csv")
type(file)

csvreader = csv.reader(file)

with open("sales.csv", mode='r') as sales_file:

    sales_reader = csv.DictReader(sales_file, delimiter=';')
    for row in sales_reader:
        print(row)

#  2. Collect all the sales from each month into a single list
Sales_by_month = []

with open("sales.csv", "r", newline="") as csvv_file:
    reader = csv.DictReader(csvv_file, delimiter=';')

    for row in reader:
        Sales_by_month.append(float(row["sales"]))

print("Sales by month: ", Sales_by_month)

#  3. Output the total sales across all months
Total_Sales = []
with open("sales.csv", "r", newline="") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')

    for col in reader:
        Total_Sales.append(float(col["sales"]))
print("Annual Revenue: ", sum(Total_Sales))


# 4. Total annual expenditure

Total_Expenditure = []
with open("sales.csv", "r", newline="") as csv_ffile:
    reader = csv.DictReader(csv_ffile, delimiter=';')

    for col in reader:
        Total_Expenditure.append(float(col["expenditure"]))
print("Annual Expenditure: ", round(sum(Total_Expenditure), 3))

# 5. Monthly changes as a percentage and export the file as csv
Sales_by_month = []

with open("sales.csv", "r", newline="") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')

    for row in reader:
        Sales_by_month.append(float(row["sales"]))

#for month in Sales_by_month:
changes = []
for i in range(1, len(Sales_by_month)):
    changes.append(round((Sales_by_month[i] - Sales_by_month[i - 1]) /  Sales_by_month[i - 1] * 100, 2))

print("Sales by month: ", Sales_by_month)
print("Monthly changes: ", changes)

# Exporting the DataFrame as a CSV file
with open('Monthly_changes.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter=',')
    # writing the data
    writer.writerow(changes)

# 6. The average annual sale
Sales = []
Average_Sales = []

with open("sales.csv", "r", newline="") as csv_ffile:
    reader = csv.DictReader(csv_ffile, delimiter=';')

    for col in reader:
        Sales.append(float(col["sales"]))

    for i in range(1, len(Sales)):
        Average_Sales = ((round(sum(Sales) / len(Sales), 3)))

print('Annual Average Sale: ', Average_Sales)

# Exporting the DataFrame as a CSV file
data = [Average_Sales]
output = 'Average_Sale.csv'

with open(output,'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter=',')
    for item in data:
        writer.writerow(data)

# 7. Month with the highest sale
with open('sales.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 2

    id_max = 0
    value_max = -math.inf # to calculate arithmetic

    for row in csv_reader:
        if line_count == 2:
            line_count += 1
        else:
            line_count += 0
            if float(row[3]) > value_max:
                id_max, value_max = row[1], float(row[2])

print(f'The month with the highest sale is {id_max} and the value is: {value_max}')

# Exporting the DataFrame as a CSV file
data = [value_max]
output = 'Highest_Sale.csv'

with open(output,'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter=',')
    for item in data:
        writer.writerow(data)

# 8. Month with the lowest sale
with open('sales.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 2

    id_min = 0
    value_min = math.inf

    for row in csv_reader:
        if line_count == 2:
            line_count += 1
        else:
            line_count += 0
            if float(row[2]) < value_min:
                id_min, value_min = row[1], float(row[2])

print(f'The month with the lowest sales is {id_min} and the value is: {value_min}')

# Exporting the DataFrame as a CSV file
data = [value_min]
output = 'Lowest_Sale.csv'

with open(output,'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter=',')
    for item in data:
        writer.writerow(data)

# 9. The average expenditure
Average_Expenditure = []
with open("sales.csv", "r", newline="") as csv_ffile:
    reader = csv.DictReader(csv_ffile, delimiter=';')

    for col in reader:
        Average_Expenditure.append(float(col["expenditure"]))
print("Annual Average Expenditure: ", round(sum(Average_Expenditure) / len(Average_Expenditure), 3))

# 10. Month with the highest expenditure
with open('sales.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 3

    id_max = 0
    value_max = -math.inf

    for row in csv_reader:
        if line_count == 3:
            line_count += 1
        else:
            line_count += 0
            if float(row[3]) > value_max:
                id_max, value_max = row[1], float(row[3])

print(f'The month with the highest expenditure is {id_max} and the value is: {value_max}')

# ○ Month with the lowest expenditure
with open('sales.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 3

    id_min = 0
    value_min = math.inf

    for row in csv_reader:
        if line_count == 3:
            line_count += 1
        else:
            line_count += 0
            if float(row[3]) < value_min:
                id_min, value_min = row[1], float(row[3])

print(f'The month with lowest expenditure is {id_min} and the value is: {value_min}')

# 12. Visualizations of the correlation between the sales & expenditures

# Import pandas and matplotlib to make the chart
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("sales.csv", delimiter=';')
df = pd.DataFrame(data)

print(df.head())

x = ["month"] # my x axis
y = ["sales"] # my y axis
z = "expenditure"
plt.plot(data.month, data.sales)
plt.plot(data.month, data.expenditure)
plt.title("Variations") # The title of the chart
plt.xlabel("month")
plt.ylabel("sales and expenditures")
plt.legend(["sales", "expenditures"])
plt.show() # Show the chart

# Close the file: "sales.csv"
file.close()
# check closed status
print(file.closed)
# Prints True



