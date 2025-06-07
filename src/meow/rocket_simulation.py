# Contains rocket dynamics and simulation logic

import math
from constants import *

def compute_mass(t):
    if t < burn_time:
        return rocket_mass - (fuel_mass * (t / burn_time))
    else:
        return rocket_mass - fuel_mass

def compute_acceleration(t):
    m = compute_mass(t)
    if t < burn_time:
        return (thrust / m) - g
    else:
        return -g

def rk4_step(v, h, t, dt):
    def f(x, v, t):
        return compute_acceleration(t)

    k1_v = f(h, v, t) * dt
    k1_h = v * dt

    k2_v = f(h + 0.5 * k1_h, v + 0.5 * k1_v, t + 0.5 * dt) * dt
    k2_h = (v + 0.5 * k1_v) * dt

    k3_v = f(h + 0.5 * k2_h, v + 0.5 * k2_v, t + 0.5 * dt) * dt
    k3_h = (v + 0.5 * k2_v) * dt

    k4_v = f(h + k3_h, v + k3_v, t + dt) * dt
    k4_h = (v + k3_v) * dt

    v_new = v + (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6
    h_new = h + (k1_h + 2*k2_h + 2*k3_h + k4_h) / 6

    return v_new, h_new

def simulate():
    t = 0
    v = 0
    h = 0
    trajectory = []

    while t <= total_time:
        trajectory.append((t, h, v))
        v, h = rk4_step(v, h, t, time_step)
        t += time_step

    return trajectory
