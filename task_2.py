import pandas as pd

df = pd.read_csv("shopping_trends.csv")

print(df.head())
print(df.info())
print(df.describe())