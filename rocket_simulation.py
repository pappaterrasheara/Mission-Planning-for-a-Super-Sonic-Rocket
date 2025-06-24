import math
from constants import *

def compute_mass(t):
    """
    Calculate rocket mass at time t considering fuel burn.
    """
    if t < burn_time:
        return rocket_mass - (fuel_mass * (t / burn_time))
    else:
        return rocket_mass - fuel_mass

def compute_acceleration(t):
    """
    Calculate acceleration at time t considering thrust and gravity.
    """
    m = compute_mass(t)
    if t < burn_time:
        return (thrust / m) - g
    else:
        return -g

def rk4_step(v, h, t, dt):
    """
    Perform one Runge-Kutta 4 integration step for velocity and altitude.
    """
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
    """
    Simulate rocket flight trajectory over total_time with time_step increments.
    Returns a list of tuples: (time, altitude, velocity, mach number).
    """
    t = 0
    v = 0
    h = 0
    trajectory = []

    while t <= total_time:
        v, h = rk4_step(v, h, t, time_step)
        mach = compute_mach(v, h)
        trajectory.append((t, h, v, mach))
        t += time_step

    return trajectory

def compute_mach(v, h):
    """
    Compute Mach number given velocity and altitude.
    Uses ISA temperature lapse rate valid below 11 km.
    """
    T = T0 - 0.0065 * h
    if T < 200:
        T = 200  # avoid non-physical low temps
    a = math.sqrt(gamma * R * T)
    return abs(v) / a
