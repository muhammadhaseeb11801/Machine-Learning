
import pandas as pd

df = pd.read_csv("data.csv")

print(df)

df["Math"] = df["Math"].astype(int)

print(df["Math"])