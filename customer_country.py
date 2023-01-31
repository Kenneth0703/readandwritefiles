# i need to program that reads the file customers.csv and produces a new file 
# containing the customer name and country they are from
import csv
infile = open("customers.csv","r")
newfile = open("customer_country.csv", "w+")
read = csv.reader(infile)
writer = csv.writer(newfile)

for row in read:
    rows = [row[1],row[2],row[4]]
    writer.writerow(rows)

