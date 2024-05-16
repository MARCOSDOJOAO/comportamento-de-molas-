import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


delta = 0.05
alpha = 1.0 / (1.0 / 3.0 + 1.0 / 2.0)
beta = -0.1
gamma = 0.5
omega = 1.5
x0 = 0.1
v0 = 0.0
initial_conditions = [x0, v0]

def duffing_system(y, t, delta, alpha, beta, gamma, omega):
    x, v = y
    dxdt = v
    dvdt = -delta * v - alpha * x - beta * x**3 + gamma * np.cos(omega * t)
    return [dxdt, dvdt]

t = np.linspace(0, 100, 1000)

solution = odeint(duffing_system, initial_conditions, t, args=(delta, alpha, beta, gamma, omega))
velocity = solution[:, 1]
acceleration = -delta * velocity - alpha * solution[:, 0] - beta * solution[:, 0]**3 + gamma * np.cos(omega * t)

plt.figure(figsize=(10, 6))
plt.plot(velocity, acceleration)
#'Gráfico de Aceleração por Velocidade - Equação de Duffing')
plt.xlabel('Velocidade (v)')
plt.ylabel('Aceleração (dv/dt)')
plt.legend()
plt.grid(True)
plt.figure(figsize=(10, 5))
plt.plot(t, solution[:, 0], label='Deslocamento (x)')
#'Sistema Oscilatório Não Linear - Equação de Duffing')
plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento (x)')
plt.legend()
plt.grid(True)
plt.plot()
plt.show()


