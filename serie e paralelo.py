import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


k1 = 3.0
k2 = 2.0
m = 1.0
x0 = 0.1
v0 = 0.0
t = np.linspace(0, 25, 250)

def mass_spring_system(y, t, m, k):
    x, v = y
    dxdt = v
    dvdt = -(k / m) * x
    return [dxdt, dvdt]

k_eq_series = 1.0 / (1.0 / k1 + 1.0 / k2)
k_eq_parallel = k1 + k2

sol_series = odeint(mass_spring_system, [x0, v0], t, args=(m, k_eq_series))
sol_parallel = odeint(mass_spring_system, [x0, v0], t, args=(m, k_eq_parallel))

plt.figure(figsize=(12, 6))

plt.plot(t, sol_series[:, 0], label='Molas em Série')

plt.plot(t, sol_parallel[:, 0], label='Molas em Paralelo')

#'Comparação entre Molas em Série e em Paralelo')
plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento (m)')
plt.legend()
plt.grid(True)
plt.show()
