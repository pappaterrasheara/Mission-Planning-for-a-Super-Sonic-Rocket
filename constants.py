# This file contains physical constants and vehicle parameters

# Physical constants
g = 9.80665  # gravitational acceleration (m/s^2)
R = 287.05   # specific gas constant for air (J/kg·K)
gamma = 1.4  # specific heat ratio for air

# Vehicle parameters
rocket_mass = 500  # kg
fuel_mass = 300    # kg
burn_time = 60     # seconds
thrust = 10000     # N

# Atmospheric conditions
T0 = 288.15  # sea level standard temperature (K)
P0 = 101325  # sea level standard pressure (Pa)

# Simulation parameters
time_step = 0.1  # seconds
total_time = 120  # seconds
