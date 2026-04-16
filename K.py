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


# zad 1
# data = pd.read_excel("imiona.xlsx")
# wynik = data.groupby("Rok")["Liczba"].sum() / 1000
# print(wynik)
# wynik.plot(figsize=(8, 6), ylabel="liczba narodzin [tys.]", xticks=wynik.index, rot=45, grid=True, title="Liczba narodzin w każdym roku")
# plt.show()

# zad 2
# data = pd.read_excel("imiona.xlsx")
# wynik = data.groupby("Plec")["Liczba"].sum()
# print(wynik)
# wynik.plot(kind="bar", rot=0, title="Całkowita liczba urodzonych chłopców i dziewczynek", ylabel="liczba narodzin", color=['purple','orange'])
# plt.show()

# zad 3
# data = pd.read_excel("imiona.xlsx")
# wynik = data.groupby(["Rok","Plec"])["Liczba"].sum().sort_index(ascending=False).head(10).groupby("Plec").sum()
# wynik2 = data[data["Rok"]>data["Rok"].max()-5].groupby("Plec")["Liczba"]
# print(wynik2)
# wynik.plot(kind="pie",autopct="%.2f %%", ylabel="liczba urodzeń",title="Całkowita liczb urodzonych chłopców i dziewczynek w ostatnich 5 latach")
# plt.show()

# zad 4

# data=pd.read_csv("zamowienia.csv", sep=";")
# wynik = data.groupby("Sprzedawca")["idZamowienia"].count()
# kolory = ['red', 'blue', 'green', 'yellow', 'pink', 'orange', 'brown', 'purple', 'gray']
# wynik.plot.barh(color=kolory,figsize=(8, 6),rot=45,title="Liczba zamówień dla poszczególnych sprzedawców",ylabel='Sprzedawca',xlabel='Liczba zamówień')
# print(wynik)
# plt.show() 
