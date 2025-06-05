# src/main.py
from rocket_simulation import runge_kutta4, rocket_derivatives
import numpy as np
import matplotlib.pyplot as plt

# Initial state: altitude, velocity, mass
initial_state = np.array([0, 0, 1050])  # alt (m), vel (m/s), mass (kg)

# Constants
t0 = 0
dt = 0.1
steps = 1000
thrust = 50000     # Newtons
burn_time = 30     # seconds
Isp = 250          # seconds

# Run simulation
result = runge_kutta4(rocket_derivatives, t0, initial_state, dt, steps, thrust, burn_time, Isp)

# Plot results
time = np.arange(0, len(result) * dt, dt)
altitudes = result[:, 0]
velocities = result[:, 1]
masses = result[:, 2]

plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(time, altitudes)
plt.title("Altitude over Time")

plt.subplot(3, 1, 2)
plt.plot(time, velocities)
plt.title("Velocity over Time")

plt.subplot(3, 1, 3)
plt.plot(time, masses)
plt.title("Mass over Time")

plt.tight_layout()
plt.show()
