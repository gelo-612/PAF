import math
import matplotlib.pyplot as plt

# korisnik unosi početnu brzinu i kut otklona
v0 = float(input("Unesite pocetnu brzinu u m/s: "))
theta = float(input("Unesite kut otklona u stupnjevima: "))

# pretvorba kuta iz stupnjeva u radijane
theta = math.radians(theta)

# konstante koje se koriste u izračunu gibanja
g = 9.81
t = 0.0
dt = 0.01
x = 0.0
y = 0.0

# listovi za spremanje vrijednosti x i y tijekom gibanja
x_list = [x]
y_list = [y]

# numeričko rješavanje diferencijalnih jednadžbi
while t <= 10.0:
    x = v0 * math.cos(theta) * t
    y = v0 * math.sin(theta) * t - 0.5 * g * t**2
    x_list.append(x)
    y_list.append(y)
    t += dt

# crtanje grafova
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

plt.tight_layout() # da se ne preklapaju grafovi, za laksu citljivost
plt.show()
