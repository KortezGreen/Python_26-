# KACPER_KIEPLIN_169701.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Zad1
df = pd.read_csv("dane-IO1.csv")
fig, axes = plt.subplots(2, 1, figsize=(10, 12))


# Zad2
filtered_df = df[df["type1"].isin(["Dark", "Fairy"])]
sns.set_palette("pastel")

# wykres słupkowy
sns.countplot(
    data=filtered_df,
    x="regions",
    hue="type1",
    ax=axes[0]
)

axes[0].set_title("Liczba pokemonów typu Dark i Fairy w regionach")
axes[0].set_xlabel("Region")
axes[0].set_ylabel("Liczba pokemonów")

axes[0].grid(True)
axes[0].legend(title="Typ")


# Zad3

# policzenie pokemonów z jednym i dwoma typami
one_type = (df["Type 2"].isna()).sum()
two_types = (df["Type 2"].notna()).sum()
sizes = [one_type, two_types]

axes[1].set_title('Typy')

axes[1].pie(
    sizes,
    labels=["Jeden typ", "Dwa typy"],
    colors=['red','green'],
    autopct="%1.1f%%",
    startangle=90
)


# Zad4
fig.suptitle("Analiza statystyk", fontsize=20)

# dopasowanie elementów
plt.tight_layout()

plt.show()

# Zad5
plt.savefig("KIEPLIN_169701.png")

