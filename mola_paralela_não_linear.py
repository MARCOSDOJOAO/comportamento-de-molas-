import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

k1_paralelo = 3.0
k2_paralelo = 2.0
m_paralelo = 1.0
c_paralelo = 0.05
F_ext_paralelo = 0.5
omega_ext_paralelo = 1.5
alpha_paralelo = k1_paralelo + k2_paralelo
beta_paralelo = -0.1

def duffing_parallel(y, t, m, c, alpha, beta, F_ext, omega_ext):
    x, v = y
    dxdt = v
    dvdt = -alpha / m * x - beta * x**3 - c / m * v + F_ext / m * np.cos(omega_ext * t)
    return [dxdt, dvdt]


x0_paralelo = 0.1
v0_paralelo = 0.0
initial_conditions_paralelo = [x0_paralelo, v0_paralelo]


t_paralelo = np.linspace(0, 100, 1000)


solution_paralelo = odeint(duffing_parallel, initial_conditions_paralelo, t_paralelo, args=(m_paralelo, c_paralelo, alpha_paralelo, beta_paralelo, F_ext_paralelo, omega_ext_paralelo))

velocities = solution_paralelo[:, 1]
accelerations = -alpha_paralelo / m_paralelo * solution_paralelo[:, 0] - beta_paralelo * solution_paralelo[:, 0]**3 - c_paralelo / m_paralelo * velocities + F_ext_paralelo / m_paralelo * np.cos(omega_ext_paralelo * t_paralelo)


plt.figure(figsize=(10, 6))
plt.plot(velocities, accelerations, label="Aceleração vs. Velocidade", linestyle='-', marker='')
#Gráfico de Aceleração por Velocidade - Sistema de Molas em Paralelo (Equação de Duffing)")
plt.xlabel("Velocidade (m/s)")
plt.ylabel("Aceleração (m/s²)")
plt.legend()
plt.grid(True)
plt.figure(figsize=(10, 6))
plt.plot(t_paralelo, solution_paralelo[:, 0], label="Deslocamento (x)")
#"Sistema de Molas em Paralelo com Amortecimento, Força Externa e Não Linearidade (Equação de Duffing)")
plt.xlabel("Tempo (s)")
plt.ylabel("Deslocamento (m)")
plt.legend()
plt.grid(True)
plt.show()
