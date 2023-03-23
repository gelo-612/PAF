import matplotlib.pyplot as plt
dt = 0.01           # Vremenski korak (s)
t_max = 10.0        # Ukupno vrijeme (s)
broj_koraka = int(t_max / dt)    # Broj koraka
# Unos sile i mase
F = float(input("Unesite iznos sile (N): "))
M = float(input("Unesite masu čestice (kg): "))
# Inicijalizacija varijabli
t = 0.0
x = 0.0
v = 0.0
a = F / M
# Inicijalizacija listi za graf
t_list = [t]
x_list = [x]
v_list = [v]
a_list = [a]

for i in range(broj_koraka):
    # Izračunavanje nove brzine i pozicije
    v += a * dt
    x += v * dt
    
    a = F / M
    
    # Dodavanje vrijednosti u listu za graf
    t += dt
    t_list.append(t)
    x_list.append(x)
    v_list.append(v)
    a_list.append(a)

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

