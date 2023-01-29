import pandas as pd
data = pd.read_csv("sales.csv")
myfile = open("salesreport.csv", "w+")
data['Total'] = data['TaxAmt']+ data['SubTotal']  + data['Freight']
id = data.loc[:, ['CustomerID', "Total"]]
id = id.groupby("CustomerID").sum()
x =data.head(10)
x = x.to_string()
myfile.write(x)
id.to_csv("salesreport.csv", index=True)
    
