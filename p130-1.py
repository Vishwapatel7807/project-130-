import pandas as pd
import csv
df = pd.read_csv("/Users/roshnipatel/Desktop/Projects(WhiteHat Jr)/project 130/dwarf_stars.csv")
print(df)
df = df.dropna()
print(df)
print(df.dtypes)

df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Radius"] = 0.102763*df["Radius"]
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] = 0.000954588*df["Mass"]

df.reset_index(drop = True,inplace=True)
df.to_csv('finaldata.csv')