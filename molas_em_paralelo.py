import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


k1_series = 3.0
k2_series = 2.0
m_series = 1.0
x0_series = 0.1
v0_series = 0.0
t_series = np.linspace(0, 100, 250)
#  m*d²x/dt² + k_eq*x = 0

# Calculando a constante de mola equivalente para molas em paralelo
k_eq_parallel_simple = k1_series + k2_series

# Função que define as equações diferenciais para o sistema de duas molas em paralelo sem amortecimento e sem força externa
def parallel_springs_system(y, t, m, k_eq):
    x, v = y
    dxdt = v
    dvdt = -(k_eq / m) * x
    return [dxdt, dvdt]

# Resolvendo a equação diferencial com odeint para o sistema de duas molas em paralelo sem amortecimento e sem força externa
sol_parallel = odeint(parallel_springs_system, [x0_series, v0_series], t_series, args=(m_series, k_eq_parallel_simple))

# Plotando a solução para o sistema de duas molas em paralelo sem amortecimento e sem força externa
plt.figure(figsize=(10, 5))
plt.plot(t_series, sol_parallel[:, 0], label='Deslocamento (m)')
plt.title('Deslocamento da Massa em um Sistema de Duas Molas em Paralelo')
plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento (m)')
plt.legend()
plt.grid(True)
plt.show()

