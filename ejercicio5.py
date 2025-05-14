import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear la figura
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.grid()

# Sol en el centro
ax.plot(0, 0, 'yo', markersize=12)

# Definir los planetas: (radio_orbita, velocidad_angular, color)
planetas = [
    (2, 0.1, 'red'),
    (4, 0.05, 'blue'),
    (6, 0.02, 'green')
]

# Inicializar datos
puntos = [ax.plot([], [], 'o', color=color)[0] for _, _, color in planetas]
trayectorias = [ax.plot([], [], '-', color=color, alpha=0.3)[0] for _, _, color in planetas]
tray_x = [[] for _ in planetas]
tray_y = [[] for _ in planetas]

def init():
    for punto, tray in zip(puntos, trayectorias):
        punto.set_data([], [])
        tray.set_data([], [])
    return puntos + trayectorias

def update(frame):
    t = frame * 0.1
    for i, (r, w, _) in enumerate(planetas):
        x = r * np.cos(w * t)
        y = r * np.sin(w * t)
        puntos[i].set_data(x, y)
        tray_x[i].append(x)
        tray_y[i].append(y)
        trayectorias[i].set_data(tray_x[i], tray_y[i])
    return puntos + trayectorias

ani = FuncAnimation(fig, update, frames=500, init_func=init,
                    interval=50, blit=True)

plt.title("Sistema Planetario Simple")
plt.show()
