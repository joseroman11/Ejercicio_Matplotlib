import matplotlib.pyplot as plt
import numpy as np
import random

# 1. Gráfico de línea simple
valores = [3, 7, 1, 5, 12]
plt.figure()
plt.plot(valores, marker='o')
plt.title('Gráfico de Línea Simple')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.show()

# 2. Gráfico de barras
cursos = ['A', 'B', 'C', 'D', 'E']
cantidad = [30, 25, 40, 20, 35]
plt.figure()
plt.bar(cursos, cantidad, color='skyblue')
plt.title('Cantidad de Estudiantes por Curso')
plt.xlabel('Curso')
plt.ylabel('Cantidad de Estudiantes')
plt.show()

# 3. Gráfico de dispersión
x_rand = [random.randint(0, 100) for _ in range(50)]
y_rand = [random.randint(0, 100) for _ in range(50)]
plt.figure()
plt.scatter(x_rand, y_rand, color='red')
plt.title('Gráfico de Dispersión')
plt.xlabel('X Aleatoria')
plt.ylabel('Y Aleatoria')
plt.grid(True)
plt.show()

# 4. Subplots
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_seno = np.sin(x)
y_cuadratica = x**2

fig, axs = plt.subplots(2)
axs[0].plot(x, y_seno)
axs[0].set_title('Función Senoidal')

axs[1].plot(x, y_cuadratica)
axs[1].set_title('Función Cuadrática')

plt.tight_layout()
plt.show()
