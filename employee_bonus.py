import pandas as pd
data = pd.read_csv('EmployeePay.csv')
df = pd.DataFrame(data)
df = df.to_string()
print(df)