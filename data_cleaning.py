import pandas as pd
import csv

df = pd.read_csv("merged_dataset.csv")

del df["Luminosity"]
del df["Distance"]

df.to_csv('main.csv')