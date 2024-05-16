# para incluir o termo da força externa F_ext * cos(omega_ext * t).
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


k1_series = 3.0
k2_series = 2.0
m_series = 1.0

x0_series = 0.1
v0_series = 0.0
t_series = np.linspace(0, 50, 250)

# Parâmetros da força externa
F_ext_parallel = 0.5  # Amplitude da força externa em N
omega_ext_parallel = 1.5  # Frequência da força externa em rad/s

# Para molas em paralelo, a constante de mola equivalente é a soma das constantes.
k_eq_parallel = k1_series + k2_series  # Esta é a constante de mola equivalente correta para molas em paralelo.

# Atualizando a função para utilizar a constante de mola correta para molas em paralelo
def parallel_springs_forced_system(y, t, m, k_eq, F_ext, omega_ext):
    x, v = y
    dxdt = v
    dvdt = -(k_eq / m) * x + (F_ext / m) * np.cos(omega_ext * t)
    return [dxdt, dvdt]

# Resolvendo a EDO para molas em paralelo com a constante de mola correta
sol_parallel_forced = odeint(parallel_springs_forced_system, [x0_series, v0_series], t_series, args=(m_series, k_eq_parallel, F_ext_parallel, omega_ext_parallel))

# Plotando a solução para o sistema de duas molas em paralelo com força externa
plt.figure(figsize=(10, 5))
plt.plot(t_series, sol_parallel_forced[:, 0], label='Deslocamento com Força Externa (m)')
plt.title('Deslocamento da Massa em um Sistema de Duas Molas em Paralelo com Força Externa')
plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento (m)')
plt.legend()
plt.grid(True)
plt.show()
