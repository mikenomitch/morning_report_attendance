import pandas as pd

df = pd.read_excel('data/MASTER.xlsx', index_row=0)
print(df.columns)

for i in df.index:
    print(df['ID'][i])
    print(df['Resident Name'][i])
