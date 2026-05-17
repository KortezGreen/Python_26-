import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

#Zad 1 + 2

# x = np.arange(1, 21)
# y = 1/x
# plt.plot(x, y, 'g>', label='f(x)=1/x', linestyle=':')
# plt.axis(([0,20,0,1]))
# plt.title('Wykres funkcji f(x) dla x [1, 20]')
# plt.ylabel("f(x)")
# plt.xlabel("x")
# plt.legend()
# plt.show()

#Zad 2

# x = np.arange(0, 30, 0.1)
# y = np.sin(x)
# z = np.cos(x)
# plt.plot(x, y, label='sin(x)')
# plt.plot(x, z, label='cos(x)')
# plt.title('Wykres funkcji sin(x) i cos(x)')
# plt.ylabel("Funkcje trygonometryczne")
# plt.xlabel("x")
# plt.legend()
# plt.show()

#zad 4

# x = np.arange(0, 30, 0.1)
# y = np.sin(x)
# z = np.sin(x)
# plt.plot(x, y+1, label='sin(x)')
# plt.plot(x, (z+1)*-1, label='sin(x)')
#
# plt.xlabel("x")
# plt.ylabel("sin(x)")
# plt.title('Wykres sin(x), sin(x)')
#
# plt.legend()
# plt.show()

#zad 5

# df = pd.read_csv('iris.data', header=None)
# print(df.head())
#
# plt.scatter(x=df[0], y=df[1], s=abs(df[0]-df[1])*5, c=df[0], cmap='viridis')
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()

#zad 6

# df=pd.read_excel('imiona.xlsx')
# fig, ax = plt.subplots(1, 3, figsize=(12,5))

# plec_suma = df.groupby('Plec')['Liczba'].sum()

# girl = df[df['Plec'] == 'K'].groupby('Rok')['Liczba'].sum()
# boy = df[df['Plec'] == 'M'].groupby('Rok')['Liczba'].sum()

# rok_suma = df.groupby('Rok')['Liczba'].sum()

# ax[0].bar(plec_suma.index,plec_suma.values,color=['red','green'])
# ax[0].set_ylabel('Liczba narodzin')
# ax[0].set_xlabel('Płeć')

# ax[1].plot(girl.index,girl.values, label='Kobiety', color='red')
# ax[1].plot(boy.index,boy.values, label='Mężczyźni',color='green')
# ax[1].set_xticks(girl.index[::1])
# ax[1].tick_params(axis='x',labelsize=9, rotation=45)

# ax[2].bar(rok_suma.index, rok_suma.values,color=['blue'])
# ax[2].set_xticks(rok_suma.index[::1])
# ax[2].tick_params(axis='x',labelsize=9, rotation=45)

# plt.tight_layout()
# plt.show()

#zad 7
# df=pd.read_csv('zamowienia.csv', sep=';')
# sumy = df.groupby('Sprzedawca')['Utarg'].sum()
# plt.figure(figsize=( 16, 16))
# plt.pie(sumy.values,labels=sumy.index, autopct='%1.1f%%')
# plt.title('Wykres')
# plt.legend()
# plt.tight_layout()
# plt.show()
