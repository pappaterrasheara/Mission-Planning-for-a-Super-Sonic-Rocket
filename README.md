# Supersonic Rocket Mission Planner

This project is a Python-based simulation and planning tool for vertical launch missions of supersonic research rockets. It allows for customizable rocket parameters, calculates key propulsion values, simulates ascent dynamics, and visualizes the trajectory. It's structured to support future expansion into more complex aerospace scenarios such as multi-stage flight, drag modeling, and angled launches.

# Project Overview

The core of the simulation is built around a 4th-order Runge-Kutta numerical integrator, which models the rocket's vertical ascent under constant thrust, varying mass, and gravity. Users input their own mission parameters—such as rocket mass, thrust, and fuel type—along with specific mission goals like maximum altitude and target Mach number. The simulation computes delta-v, burn time, and continuously updates altitude, velocity, and Mach number over the flight timeline.

The goal is to provide a solid base for realistic mission planning with high customizability, simple input handling, and meaningful output visualizations.

# Relevance to Aerospace Engineering
This project introduces foundational concepts in flight dynamics and rocket mission planning — both critical in real-world aerospace design. Although simplified, the program mimics aspects of professional tools used during preliminary mission planning stages.

# It provides insight into:

- The relationship between thrust, mass, and trajectory
- Effects of fuel selection on mission performance
- The value of numerical integration in modeling dynamic systems
- The role of modular software design in engineering workflows

In future aerospace applications, similar simulations can feed into more advanced stages of design such as structural analysis, control systems, and even hardware-in-the-loop testing. The project lays a groundwork that’s extendable toward more complex multi-stage systems, orbital mechanics, or high-speed flight planning.


# Student: Sheara Isabella Pappaterra Tolentino
# BJU Homeschool ID: [12850982]
# High School Senior, AP Curriculum – Pursuing Aerospace Engineering 