import numpy as np
import matplotlib.pyplot as plt

# Konstante
G = 6.67408e-11  # Gravitacijska konstanta [Nm^2/kg^2]
MS = 1.989e30  # Masa Sunca [kg]
MZ = 5.9742e24  # Masa Zemlje [kg]
AU = 1.486e11  # Astronomska jedinica [m]
v_perpendicular = 29783  # Okomita komponenta brzine Zemlje [m/s]
year = 365.242 * 24 * 60 * 60  # Jedna godina [s]

# Početni uvjeti
x_sun = np.array([0.0, 0.0])  # Početna pozicija Sunca
x_earth = np.array([AU, 0.0])  # Početna pozicija Zemlje
v_earth = np.array([0.0, v_perpendicular])  # Početna brzina Zemlje

# Vremenski korak i broj koraka
dt = 3600  # Vremenski korak [s]
num_steps = int(year / dt)  # Broj koraka

# Pohranjivanje putanja
sun_path = np.zeros((num_steps, 2))
earth_path = np.zeros((num_steps, 2))

# Eulerova metoda
for i in range(num_steps):
    # Računanje sile na Zemlju
    r = x_sun - x_earth
    F = (G * MS * MZ / np.linalg.norm(r)**3) * r

    # Promjena brzine i pozicije Zemlje
    v_earth += (F / MZ) * dt
    x_earth += v_earth * dt

    # Pohrana pozicije
    sun_path[i] = x_sun
    earth_path[i] = x_earth

# Crtanje putanja
plt.figure(figsize=(10, 10))
plt.plot(sun_path[:, 0], sun_path[:, 1], 'r', label='Sunce')
plt.plot(earth_path[:, 0], earth_path[:, 1], 'b', label='Zemlja')
plt.scatter(0, 0, color='yellow', marker='o', label='Ishodište (Sunce)')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Putanja Sunca i Zemlje')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
