#pandas stubs

import pandas as pd
import numpy as np
import seaborn as sns

#zad 1
df = pd.read_excel('imiona.xlsx')
#print(df)
#zad 2
#a
#print(df[df['Liczba']>1000])
#b
#print(df[df['Imie']=='KACPER'])
#c
#suma=df['Liczba'].sum()
#print(suma)
#d
#print(df.groupby('Rok')['Liczba'].sum())
#e
#filtr=df[df['Rok'].between(2000, 2005)]
#print(filtr.groupby('Rok')['Liczba'].sum())
#f
#print(df.groupby('Plec')['Liczba'].sum())
#g
#print(df[df['Plec'] == 'K'].groupby('Imie')['Liczba'].sum().idxmax(),df[df['Plec'] == 'M'].groupby('Imie')['Liczba'].sum().idxmax())
#h
#print(df.loc[df.groupby(['Rok', 'Plec'])['Liczba'].idxmax()])

