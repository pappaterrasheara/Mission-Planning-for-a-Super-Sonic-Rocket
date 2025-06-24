# Entry point to run the simulation and export results.

from rocket_simulation import *
import csv
import matplotlib.pyplot as plt

def main():
    trajectory = simulate()

    # Save to CSV
    with open("rocket_trajectory.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Time (s)", "Altitude (m)", "Velocity (m/s)", "Mach"])
        writer.writerows(trajectory)

    # Plot results
    time = [row[0] for row in trajectory]
    altitude = [row[1] for row in trajectory]
    velocity = [row[2] for row in trajectory]
    mach = [row[3] for row in trajectory]

    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.plot(time, altitude)
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.title("Rocket Altitude vs Time")
    plt.grid(True)

    plt.subplot(1, 3, 2)
    plt.plot(time, velocity)
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.title("Rocket Velocity vs Time")
    plt.grid(True)

    plt.subplot(1, 3, 3)
    plt.plot(time, mach, color='purple')
    plt.xlabel("Time (s)")
    plt.ylabel("Mach Number")
    plt.title("Rocket Mach Number vs Time")
    plt.grid(True)

    plt.tight_layout()
    plt.show()
    print(f"Max Mach: {max(mach):.2f}")

if __name__ == "__main__":
    main()
