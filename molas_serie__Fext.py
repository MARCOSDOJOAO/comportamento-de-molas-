import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


k1_series = 3.0
k2_series = 2.0
m_series = 1.0

x0_series = 0.1
v0_series = 0.0
t_series = np.linspace(0, 50, 250)
F_ext_series = 0.5
omega_ext_series = 1.5

k_eq_series = 1.0 / (1.0 / k1_series + 1.0 / k2_series)
def series_springs_forced_system(y, t, m, k_eq, F_ext, omega_ext):
    x, v = y
    dxdt = v
    dvdt = -(k_eq / m) * x + (F_ext / m) * np.cos(omega_ext * t)
    return [dxdt, dvdt]

sol_series_forced = odeint(series_springs_forced_system, [x0_series, v0_series], t_series, args=(m_series, k_eq_series, F_ext_series, omega_ext_series))


plt.figure(figsize=(10, 5))
plt.plot(t_series, sol_series_forced[:, 0], label='Deslocamento com Força Externa (m)')
plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento (m)')
plt.legend()
plt.grid(True)
plt.show()
