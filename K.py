import numpy as np
import pandas as pd

df = pd.read_csv('powtorzenie.csv', sep=';')
#print(df)

#1
df = df.dropna(axis=1,how='all')
#print(df)

#2
df2 = df[df["wiek"] > 20]["wynik"].mean()
#print(df2)

#3
df['test zaliczony'] = df['wynik'] >= 50
#print(df)

#4
df4=df.groupby('test zaliczony')['wiek'].mean()
#print(df4)

#5
df5= df[df["test zaliczony"] & (df["wiek"] == df[df['test zaliczony']]['wiek'].min())][['imie']]
print(df5)
