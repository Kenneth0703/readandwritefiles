import pandas as pd
data = pd.read_csv("sales.csv")
myfile = open("salesreport.csv", "w+")
data['Total'] = data['TaxAmt']+ data['SubTotal']  + data['Freight']
id = data.loc[:, ['CustomerID', "Total"]]
id = id.groupby("CustomerID").sum()
id = id.round(2)    
id = id.reset_index()
id.to_csv("salesreport.csv", index=True)
