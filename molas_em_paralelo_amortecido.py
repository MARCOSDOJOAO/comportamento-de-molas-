import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


k1_series = 3.0
k2_series = 2.0
m_series = 1.0
k_eq_series = 1.0 / (1.0 / k1_series + 1.0 / k2_series)
x0_series = 0.1
v0_series = 0.0
c_series = 0.05

k_eq_parallel = k1_series + k2_series
t_series = np.linspace(0, 100, 250)

def parallel_springs_damped_system(y, t, m, k_eq, c):
    x, v = y
    dxdt = v
    dvdt = -(k_eq / m) * x - (c / m) * v
    return [dxdt, dvdt]


sol_parallel_damped = odeint(parallel_springs_damped_system, [x0_series, v0_series], t_series, args=(m_series, k_eq_parallel, c_series))


plt.figure(figsize=(10, 5))
plt.plot(t_series, sol_parallel_damped[:, 0], label='Deslocamento com Amortecimento (m)')
plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento (m)')
plt.legend()
plt.grid(True)
plt.show()
