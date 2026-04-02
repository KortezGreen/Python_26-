import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.conftest import ascending

#zad 1
# data = np.random.randint(0, 101, size=(20, 5))
# columns = ['Matematyka', 'Chemia', 'Fizyka', 'Biologia', 'Informatyka']
# df = pd.DataFrame(data, columns=columns)
# df['Średnia'] = df.mean(axis=1)
#
# def przypisz_ocene(srednia):
#     if srednia >= 81: return 5
#     if srednia >= 61: return 4
#     if srednia >= 41: return 3
#     if srednia >= 0: return 2
#     return 1
#
# df['Ocena'] = df['Średnia'].apply(przypisz_ocene)
# print(df.head())
# df.to_excel("oceny.xlsx", index=False)

#zad 2
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack'],
    'Punktacja [%]': [85, 90, 78, np.nan, 88, 76, 92, np.nan, 80, 84],
    'Frekwencja [%]': [95, 85, np.nan, 75, 88, 92, 89, 80, np.nan, 91],
    'Zaj_dodatkowe': [True, True, False, True, False, False, False, True, False, False]
}
df = pd.DataFrame(data)
df.loc[10] = ['Maria', 93.0, 75.0, True]
df.loc[df['Student'] == 'Frank', 'Zaj_dodatkowe'] = True
# print('Przed')
# print(df[df.isnull().any(axis=1)])
# print('Po')
df.fillna(100, inplace=True)
# print(df)
df.to_csv("new_data.csv", index=False)

#f
# wynik = df[df['Punktacja [%]'] > 85]
# print(wynik)

#g
# wynik = df['Frekwencja [%]'].mean()
# print(wynik)

#h
# wynik = df.sort_values(['Punktacja [%]','Frekwencja [%]'], ascending=[False,True])
# print(wynik)

#i
# wynik = df.groupby('Zaj_dodatkowe')['Frekwencja [%]'].median()
# print(wynik)

#j
df['Punktacja_norm'] = (df['Punktacja [%]'] - np.min(df['Punktacja [%]'])) / (np.max(df['Punktacja [%]']) - np.min(df['Punktacja [%]']))
plt.figure(figsize=(10, 6))
plt.plot(df['Student'], df['Punktacja_norm'], marker='o', linestyle='-', color='steelblue', label='Punktacja norm')
plt.title('Wyniki studentów (normalizowane)')
plt.xlabel('Student')
plt.grid()
plt.legend()
plt.show()
