# KACPER_KIEPLIN_169701.py

# =========================
# Zad1
# =========================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# wczytanie danych
df = pd.read_csv("dane-IO1.csv")

# utworzenie ryciny: 1 kolumna, 2 rzędy
fig, axes = plt.subplots(2, 1, figsize=(10, 12))

# =========================
# Zad2
# =========================

# filtrowanie typów Dark i Fairy
filtered_df = df[df["type1"].isin(["Dark", "Fairy"])]

# ustawienie palety pastelowej
sns.set_palette("pastel")

# wykres słupkowy
sns.countplot(
    data=filtered_df,
    x="regions",
    hue="type1",
    ax=axes[0]
)

# opis wykresu
axes[0].set_title("Liczba pokemonów typu Dark i Fairy w regionach")
axes[0].set_xlabel("Region")
axes[0].set_ylabel("Liczba pokemonów")

# siatka
axes[0].grid(True)

# legenda
axes[0].legend(title="Typ")

# =========================
# Zad3
# =========================

# policzenie pokemonów z jednym i dwoma typami
one_type = (df["type2"].isna()).sum()
two_types = (df["type2"].notna()).sum()

sizes = [one_type, two_types]
labels = ["Jeden typ", "Dwa typy"]

# wybrane kolory
colors = ["lightblue", "lightcoral"]

# wykres kołowy
axes[1].pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90
)

axes[1].set_title(
    "Procentowy udział pokemonów z jednym i dwoma typami"
)

# =========================
# Zad4
# =========================

fig.suptitle("Analiza statystyk", fontsize=20)

# dopasowanie elementów
plt.tight_layout()

# =========================
# Zad5
# =========================

plt.savefig("KIEPLIN_169701.png")

# brak plt.show()
