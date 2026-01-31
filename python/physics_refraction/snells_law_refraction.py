"""
Physics Simulation: Refraction of Light using Snell's Law
Demonstrates angle of refraction and ray diagram

"""
import numpy as np
import matplotlib.pyplot as plt

# INPUT VALUES

n1 = float(input("enter the refractive index of MEDIUM 1:"))        # Refractive index of medium 1
n2 = float(input("enter the refractive index of MEDIUM 2:"))       # Refrcative index of medium 2
i_deg = float(input("enter the angle of incidence in degrees:"))      # Angle of incidence in degrees

i_rad = np.radians(i_deg)

# Snell's Law(formula
sin_r = (n1 / n2) * np.sin(i_rad)

# Check for total internal reflection
if sin_r >= 1:
    print("Total Internal Reflection occurs")
    exit()

r_rad = np.arcsin(sin_r)
r_deg = np.degrees(r_rad)


# PRINT RESULTS

print("Angle of Incidence (i):", i_deg, "degrees")
print("Angle of Refraction (r):", round(r_deg, 2), "degrees")
print("n1 sin(i) =", round(n1 * np.sin(i_rad), 4))
print("n2 sin(r) =", round(n2 * np.sin(r_rad), 4))
#--------------
# RAY DIAGRAM
#--------------
# Incident ray
x_inc = np.linspace(-5, 0, 100)
y_inc = np.tan(i_rad) * x_inc

# Refracted ray
x_ref = np.linspace(0, 5, 100)
y_ref = np.tan(r_rad) * x_ref

plt.figure()
plt.plot(x_inc, y_inc, label="Incident Ray")
plt.plot(x_ref, y_ref, label="Refracted Ray")

# Boundary and normal
plt.axvline(0, linestyle='--', label="Boundary")
plt.axhline(0, linestyle=':')

plt.text(-4, 2, f"i = {i_deg}°")
plt.text(1, 1, f"r = {round(r_deg,2)}°")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Refraction of Light (Snell's Law)")
plt.legend()
plt.grid()
plt.show()


"""
Sample Input:
enter the refractive index of MEDIUM 1: 1.0
enter the refractive index of MEDIUM 2: 1.5
enter the angle of incidence in degrees: 30

Sample Output:
Angle of Incidence (i): 30 degrees
Angle of Refraction (r): 19.47 degrees
n1 sin(i) = 0.5
n2 sin(r) = 0.5
"""
