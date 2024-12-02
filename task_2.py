import pandas as pd

df = pd.read_csv("dz.csv")

print(df.head())

print(df.groupby("City")["Salary"].mean())
