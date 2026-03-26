import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
# wynik2= data[data["Rok"]>2012].groupby("Plec")["Liczba"]
# print(wynik2)
# wynik.plot(kind="pie",autopct="%.2f %%", ylabel="liczba urodzeń",title="Całkowita liczb urodzonych chłopców i dziewczynek w latach 2013-2017")
# plt.show()

# zad 4

# data=pd.read_csv("zamowienia.csv", sep=";")
# wynik = data.groupby("Sprzedawca")["idZamowienia"].count()
# kolory = ['red', 'blue', 'green', 'yellow', 'pink', 'orange', 'brown', 'purple', 'gray']
# wynik.plot.barh(color=kolory,figsize=(8, 6),rot=45,title="Liczba zamówień dla poszczególnych sprzedawców",ylabel='Sprzedawca',xlabel='Liczba zamówień')
# print(wynik)
# plt.show()
