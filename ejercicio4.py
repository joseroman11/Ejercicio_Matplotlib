import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Cargar datos
df = pd.read_csv("datos.csv")
years = df["Año"].tolist()
countries = df.columns[1:]
values = df.iloc[:, 1:].values

fig, ax = plt.subplots()
bars = ax.bar(countries, values[0])
ax.set_ylim(0, values.max() * 1.1)
title = ax.set_title("")

def update(i):
    for bar, height in zip(bars, values[i]):
        bar.set_height(height)
    title.set_text(f"Año: {years[i]}")
    return bars

ani = FuncAnimation(fig, update, frames=len(values), interval=1000, repeat=True)
plt.title("Evolución de Datos por País")
plt.show()
