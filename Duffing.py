import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


A = 3  # Amplitude inicial
v0 = 0  # Velocidade inicial
omega_n = 1.0
zeta = 0.05
F = 1.0
omega = 1.2 * omega_n
alpha = 1.0
y0 = [A, v0]
t_max = 50
num_points = 5000
t = np.linspace(0, t_max, num_points)


def duffing(y, t, zeta, omega_n, F, omega, alpha):
    x, x1 = y
    dxdt = x1
    dx1dt = -2 * zeta * omega_n * x1 - omega_n**2 * x - alpha * x**3 + F * np.cos(omega * t)
    return [dxdt, dx1dt]


sol_duffing = odeint(duffing, y0, t, args=(zeta, omega_n, F, omega, alpha))

# Plotando a solução
plt.figure(figsize=(12, 6))
plt.plot(t, sol_duffing[:, 0], label='Oscilador de Duffing')
#'Oscilador de Duffing com termo não linear')
plt.xlabel('Tempo')
plt.ylabel('Deslocamento (x)')
plt.grid(True)
plt.legend()
plt.show()


aceleracao_duffing = -2 * zeta * omega_n * sol_duffing[:, 1] - omega_n**2 * sol_duffing[:, 0] - alpha * sol_duffing[:, 0]**3 + F * np.cos(omega * t)

# Agora podemos plotar a aceleração em função da velocidade
plt.figure(figsize=(10, 6))
plt.plot(sol_duffing[:, 1], aceleracao_duffing, label='Aceleração vs. Velocidade')
#'Espaço de Fase (Aceleração vs. Velocidade)')
plt.xlabel('(dx/dt)')
plt.ylabel(' (d²x/dt²)')
plt.grid(True)
plt.legend()
plt.show()
