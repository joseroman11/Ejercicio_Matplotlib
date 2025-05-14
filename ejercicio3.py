import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Preparar figura
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid()

# Punto rojo y trayectoria azul
point, = ax.plot([], [], 'ro')
trail, = ax.plot([], [], 'b-', alpha=0.5)

trail_x, trail_y = [], []

def init():
    point.set_data([], [])
    trail.set_data([], [])
    return point, trail

def update(frame):
    t = frame * 0.1  # velocidad angular
    x = np.cos(t)
    y = np.sin(t)
    trail_x.append(x)
    trail_y.append(y)
    point.set_data(x, y)
    trail.set_data(trail_x, trail_y)
    return point, trail

ani = FuncAnimation(fig, update, frames=300, init_func=init,
                    interval=50, blit=True)

plt.title("Movimiento Circular con Trayectoria")
plt.show()
