# i need to program that reads the file customers.csv and produces a new file 
# containing the customer name and country they are from
import pandas as pd
myfile = open("customers and countries.csv", "w+")
data = pd.read_csv('customers.csv')
x = (data.filter(regex='Name|Country'))
x= x.to_string()
myfile.write(x)


