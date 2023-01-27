import pandas as pd
myfile = open("salesreport.csv", "w+")
data = pd.read_csv('sales.csv')
x = (data.filter(regex='CustomerID'))
q = (data.filter(regex='SubTotal'))
w = (data.filter(regex='TaxAmt'))
e = (data.filter(regex='Freight'))
#data.sum(SubTotal,TaxAmt,Freight)
#grouped_data = data.groupby("CustomerID").sum({"SubTotal"+"TaxAmt"+"Freight"}

data = data.rename(columns={'SubTotal': "Total"})
grouped_data = data.groupby("CustomerID").sum("Total")
grouped_data = grouped_data.to_string()
myfile.write(grouped_data)
y = (data.filter(regex='SubTotal|TaxAmt|Freight'))