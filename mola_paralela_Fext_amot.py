import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
k1_series = 3.0
k2_series = 2.0
m_series = 1.0

# Parâmetros para amortecimento e força externa
c_parallel = 0.05  # Coeficiente de amortecimento em Ns/m
F_ext_parallel = 0.5  # Amplitude da força externa em N
omega_ext_parallel = 1.5  # Frequência da força externa em rad/s

# Atualização da constante de mola equivalente para o sistema em paralelo
k_eq_parallel = k1_series + k2_series

# Definindo a função do sistema em paralelo com amortecimento e força externa
def parallel_springs_damped_forced_system(y, t, m, k_eq, c, F_ext, omega_ext):
    x, v = y
    dxdt = v
    dvdt = -(k_eq / m) * x - (c / m) * v + (F_ext / m) * np.cos(omega_ext * t)
    return [dxdt, dvdt]

# Intervalo de tempo
t_parallel = np.linspace(0, 500, 250)  # 50 segundos, 250 pontos

# Condições iniciais
x0_parallel = 0.1  # Deslocamento inicial em metros
v0_parallel = 0.0  # Velocidade inicial em m/s

# Resolvendo a EDO para o sistema em paralelo com amortecimento e força externa
sol_parallel_damped_forced = odeint(parallel_springs_damped_forced_system, [x0_parallel, v0_parallel], t_parallel, args=(m_series, k_eq_parallel, c_parallel, F_ext_parallel, omega_ext_parallel))

# Plotando a solução para o sistema em paralelo com amortecimento e força externa
plt.figure(figsize=(10, 5))
plt.plot(t_parallel, sol_parallel_damped_forced[:, 0], label='Deslocamento com Amortecimento e Força Externa')
#'Sistema de Duas Molas em Paralelo: Amortecido e com Força Externa')
plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento (m)')
plt.legend()
plt.grid(True)
plt.show()
