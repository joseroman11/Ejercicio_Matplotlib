import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 1000)
line, = ax.plot(x, np.sin(x))

def update(t):
    line.set_ydata(np.sin(x + t))  # fase desplazada
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), interval=50)
plt.title("Onda Senoidal con Fase Desplazada")
plt.grid()
plt.show()
