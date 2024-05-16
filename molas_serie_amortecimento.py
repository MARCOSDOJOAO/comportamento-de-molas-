import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


k1_series = 3.0
k2_series = 2.0
m_series = 1.0


k_eq_series = 1.0 / (1.0 / k1_series + 1.0 / k2_series)


x0_series = 0.1  # Deslocamento inicial em metros
v0_series = 0.0  # Velocidade inicial em m/s
t_series = np.linspace(0, 100, 250)
c_series = 0.05


def series_springs_damped_system(y, t, m, k_eq, c):
    x, v = y
    dxdt = v
    dvdt = -(k_eq / m) * x - (c / m) * v
    return [dxdt, dvdt]


sol_series_damped = odeint(series_springs_damped_system, [x0_series, v0_series], t_series, args=(m_series, k_eq_series, c_series))


plt.figure(figsize=(10, 5))
plt.plot(t_series, sol_series_damped[:, 0], label='Deslocamento com Amortecimento (m)')
plt.title('Deslocamento da Massa em um Sistema de Duas Molas em Série com Amortecimento')
plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento (m)')
plt.legend()
plt.grid(True)
plt.show()
