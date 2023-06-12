import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, m, k, x0, v0):
        self.m = m
        self.k = k
        self.x = x0
        self.v = v0

    def e(self):#energija 
        return 0.5 * self.m * self.v**2 + 0.5 * self.k * self.x**2

    def akc(self):#akceleracija
        return -self.k / self.m * self.x

    def update(self, dt):
        a = self.akc()
        self.x += self.v * dt
        self.v += a * dt

    def simultiranje(self, t, dt):
        koraci = int(t / dt)
        putanja = np.zeros((koraci, 2))
        for i in range(koraci):
            putanja[i, 0] = self.x
            putanja[i, 1] = self.v
            self.update(dt)
        return putanja

    def racun_period(self, dt):
        x_p = self.x
        t = 0
        while True:
            self.update(dt)
            if (self.x > 0 and x_p < 0) or (self.x < 0 and x_p > 0):
                t_period = 2 * t
                break
            t += dt
            x_p = self.x
        return t_period

# Primjer ispitivanja preciznosti numeričkog rješenja za različite korake ∆t
m = 1.0  # masa
k = 1.0  # konstanta opruge
x0 = 1.0  # početni položaj
v0 = 0.0  # početna brzina
t = 10.0  # vrijeme simulacije
dt_vrijednosti = [0.1, 0.05, 0.01, 0.005, 0.001] 

# Stvaranje instance klase HarmonicOscillator s početnim uvjetima
oscillator = HarmonicOscillator(m, k, x0, v0)

# Računanje perioda titranja za različite korake ∆t
periodi = []
for dt in dt_vrijednosti:
    oscillator.x = x0
    oscillator.v = v0
    period = oscillator.racun_period(dt)
    periodi.append(period)
    print( 'dt={},period={}'.format(dt,period))

# Crtanje grafika preciznosti u ovisnosti o veličini koraka ∆t
fig, ax = plt.subplots(figsize=(8, 6))
ax.loglog(dt_vrijednosti, periodi, '-o')
ax.set_xlabel('dt')
ax.set_ylabel('period')
ax.set_title('Preciznost numeričkog računanja perioda titranja')
plt.show()
