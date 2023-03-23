import matplotlib.pyplot as plt
import numpy as np
import math
def jednolikogibanje(F,M):
    dt = 0.01
    t_max = 10.0        
    broj_koraka = int(t_max / dt)    
    F = float(input("Unesite iznos sile (N): "))
    M = float(input("Unesite masu čestice (kg): "))
    t = 0.0
    x = 0.0
    v = 0.0
    a = F / M
    t_list = [t]
    x_list = [x]
    v_list = [v]
    a_list = [a]

    for i in range(broj_koraka):
        v += a * dt
        x += v * dt
    
        a = F / M
    
        t += dt
    t_list.append(t)
    x_list.append(x)
    v_list.append(v)
    a_list.append(a)
jednolikogibanje(50.0,0.3)        


fig, axs = plt.subplots(3, 1, figsize=(8, 10))
axs[0].plot(t_list, x_list)
axs[0].set_xlabel("Vrijeme (s)")
axs[0].set_ylabel("Pozicija (m)")
axs[1].plot(t_list, v_list)
axs[1].set_xlabel("Vrijeme (s)")
axs[1].set_ylabel("Brzina (m/s)")
axs[2].plot(t_list, a_list)
axs[2].set_xlabel("Vrijeme (s)")
axs[2].set_ylabel("Ubrzanje (m/s^2)")

plt.show()
def kosihitac(v0,theta):
    v0 = float(input("Unesite pocetnu brzinu u m/s: "))
    theta = float(input("Unesite kut otklona u stupnjevima: "))

    theta = math.radians(theta)

    g = 9.81
    t = 0.0
    dt = 0.01
    x = 0.0
    y = 0.0

    x_list = [x]
    y_list = [y]

    while t <= 10.0:
        x = v0 * math.cos(theta) * t
        y = v0 * math.sin(theta) * t - 0.5 * g * t**2
        x_list.append(x)
        y_list.append(y)
        t += dt
kosihitac(25,60)

plt.figure(figsize=(10, 10))

plt.subplot(311)
plt.plot(x_list, y_list)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("x-y graf")

plt.subplot(312)
plt.plot(x_list, [t*dt for t in range(len(x_list))])
plt.xlabel("x (m)")
plt.ylabel("t (s)")
plt.title("x-t graf")

plt.subplot(313)
plt.plot(y_list, [t*dt for t in range(len(y_list))])
plt.xlabel("y (m)")
plt.ylabel("t (s)")
plt.title("y-t graf")

plt.tight_layout() 
plt.show()

import kinematika as kin

kin.jednolikogibanje(50.0,0.3)
kin.kosihitac(25,60)