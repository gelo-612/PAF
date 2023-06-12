import numpy as np

class HarmonicOscillator:
    def __init__(self, x, v, A, omega, phi, dt):
        self.x = x
        self.v = v
        self.A = A
        self.omega = omega
        self.phi = phi
        self.dt = dt
    
    def pozicija(self, t):
        return self.A * np.sin(self.omega * t + self.phi)
    
    def brzina(self, t):
        return self.A * self.omega * np.cos(self.omega * t + self.phi)
    
    def akceleracija(self, t):
        return -self.A * self.omega**2 * np.sin(self.omega * t + self.phi)
    
    def kin_energ(self, t):
        return 0.5 * self.v**2
    
    def pot_energ(self, t):
        return 0.5 * self.A**2 * self.omega**2 * np.sin(self.omega * t + self.phi)**2
    
    def energ(self, t):
        return self.kin_energ(t) + self.pot_energ(t)
    
    def razvoj(self):
        self.x += self.v * self.dt
        self.v += self.akceleracija(0) * self.dt

import matplotlib.pyplot as plt

ho = HarmonicOscillator(x=1, v=0, A=2, omega=1, phi=0, dt=0.01)
t = np.arange(0, 10, ho.dt)

x = [ho.pozicija(ti) for ti in t]
v = [ho.brzina(ti) for ti in t]
a = [ho.akceleracija(ti) for ti in t]

fig, axs = plt.subplots(3, 1, figsize=(8, 12))
axs[0].plot(t, x)
axs[0].set_xlabel('t')
axs[0].set_ylabel('x')
axs[0].set_title('x-t graf')

axs[1].plot(t, v)
axs[1].set_xlabel('t')
axs[1].set_ylabel('v')
axs[1].set_title('v-t graf')

axs[2].plot(t, a)
axs[2].set_xlabel('t')
axs[2].set_ylabel('a')
axs[2].set_title('a-t graf')

plt.show()

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

for dt in [0.1, 0.01, 0.001]:
    ho = HarmonicOscillator(x=1, v=0, A=2, omega=1, phi=0, dt=dt)
    t = np.arange(0, 10, ho.dt)
    x = [ho.pozicija(ti) for ti in t]
    v = [ho.brzina(ti) for ti in t]
    a = [ho.akceleracija(ti) for ti in t]
    axs[0].plot(t, x, label=f'dt={dt}')
    axs[1].plot(t, v, label=f'dt={dt}')
    axs[2].plot(t, a, label=f'dt={dt}')

axs[0].set_xlabel('t')
axs[0].set_ylabel('x')
axs[0].set_title('x-t graf')
axs[0].legend()

axs[1].set_xlabel('t')
axs[1].set_ylabel('v')
axs[1].set_title('v-t graf')
axs[1].legend()

axs[2].set_xlabel('t')
axs[2].set_ylabel('a')
axs[2].set_title('a-t graf')
axs[2].legend()

plt.show()

