import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

num_points = 100
positions = np.random.rand(num_points, 2)

fig, ax = plt.subplots()
sc = ax.scatter(positions[:, 0], positions[:, 1])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

def update(frame):
    # Movimiento aleatorio pequeño
    displacement = 0.01 * (np.random.rand(num_points, 2) - 0.5)
    positions[:] += displacement
    positions[:] = np.clip(positions, 0, 1)
    sc.set_offsets(positions)
    return sc,

ani = FuncAnimation(fig, update, frames=200, interval=50)
plt.title("Partículas en Movimiento Aleatorio")
plt.show()
