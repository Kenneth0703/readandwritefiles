import csv
#infile = open("EmployeePay.csv","r") 
with open("EmployeePay.csv","r") as csv_input:

    reader = csv.reader(csv_input)
    for row in reader:
        print(row)



