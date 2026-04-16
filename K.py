import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr=np.array([[0,1,2,3],[10,11,12,13],[40,41,42,43]])
arr[:2, 1]= -3
print(arr)
sred = np.sum(arr>25)
print(sred)
arr[arr%2==0] = 0
print(arr)
mat = np.zeros((7, 7), dtype=int)

np.fill_diagonal(mat, 3)
np.fill_diagonal(mat[1:], -1)   # pod główną
np.fill_diagonal(mat[:, 1:], -1)  # nad główną

print(mat) 



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
