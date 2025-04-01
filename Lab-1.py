import numpy as np
import matplotlib.pyplot as plt

# Updated Constants
K1 = 0.02   # Reaction rate constant for the decrease of C1 and C2
K2 = 0.008  # Reaction rate constant for the increase of C3
DT = 0.01   # Time step
TIME = 200.0  # Total simulation time in seconds

# Updated Initial concentrations
C1 = [100.0]
C2 = [60.0]
C3 = [10.0]

# Time initialization
time = [0.0]

# Simulation loop
while time[-1] < TIME:
    t = time[-1]
    c1 = C1[-1]
    c2 = C2[-1]
    c3 = C3[-1]

    # Calculate next values
    c1_next = c1 + ((K2 * c3 - K1 * c1 * c2) * DT)
    c2_next = c2 + ((K2 * c3 - K1 * c1 * c2) * DT)
    c3_next = c3 + (2.0 * (K1 * c1 * c2 - K2 * c3) * DT)

    # Append new values
    C1.append(c1_next)
    C2.append(c2_next)
    C3.append(c3_next)
    time.append(t + DT)

# Plot the results
plt.figure(figsize=(7, 4))
plt.plot(time, C1, label="Concentration of C1", color="red")   # C1 in Red
plt.plot(time, C2, label="Concentration of C2", color="blue")  # C2 in Blue
plt.plot(time, C3, label="Concentration of C3", color="green") # C3 in Green

plt.xlabel("Time (s)")
plt.ylabel("Concentration")
plt.title("Nabin Joshi Scatter Plot of Chemical Reaction")
plt.legend()
plt.grid()
plt.show()