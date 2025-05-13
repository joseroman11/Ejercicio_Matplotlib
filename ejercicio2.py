import numpy as np
import matplotlib.pyplot as plt

# 5. Generar datos y graficar función cuadrática
x = np.linspace(-10, 10, 100)
y = x**2 - 3*x + 2
plt.figure()
plt.plot(x, y, label='y = x² - 3x + 2')
plt.title('Función Cuadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

# 6. Comparación de sin(x) y cos(x)
x = np.linspace(0, 2 * np.pi, 100)
sin_x = np.sin(x)
cos_x = np.cos(x)

plt.figure()
plt.plot(x, sin_x, label='sin(x)', color='blue')
plt.plot(x, cos_x, label='cos(x)', color='green')
plt.title('Comparación entre sin(x) y cos(x)')
plt.xlabel('x')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()

# 7. Estadísticas con números aleatorios
vector = np.random.randint(0, 101, 100)
suma_total = np.sum(vector)
valor_maximo = np.max(vector)
desviacion = np.std(vector)

print("Suma total:", suma_total)
print("Valor máximo:", valor_maximo)
print("Desviación estándar:", desviacion)

# 8. Histograma de distribución normal
normal_data = np.random.normal(loc=0, scale=1, size=1000)

plt.figure()
plt.hist(normal_data, bins=30, color='purple', alpha=0.7, edgecolor='black')
plt.title('Histograma de Distribución Normal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()
