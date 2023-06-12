import numpy as np
import matplotlib.pyplot as plt
import math 

class Particle:
    def __init__(self, v, kut, pozicija):
        self.v = v
        self.kut = kut
        self.pozicija = pozicija
        self.reset()
    
    def reset(self):
        self.time_elapsed = 0.0
        self.x_poz = [self.pozicija[0]]
        self.y_poz = [self.pozicija[1]]
        self.vx = self.v * np.cos(self.kut)
        self.vy = self.v * np.sin(self.kut)
    
    def __move(self, dt):
        self.x_poz.append(self.x_poz[-1] + self.vx * dt)
        self.y_poz.append(self.y_poz[-1] + self.vy * dt)
        self.vy = self.vy - 9.81 * dt
    
    def range(self, dt):
        while self.y_poz[-1] > 0:
            self.__move(dt)
        return self.x_poz[-1]
    
    def plot_trajectory(self):
        plt.plot(self.x_poz, self.y_poz)
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title('Projectile trajectory')
        plt.show()


    def domet_analiticki(self):
        g = 9.81
        d = (self.v**2/g) * math.sin(2*math.radians(self.kut))
        return d

    def odstupanje(self, dt):
        print(abs(self.range(dt) - self.domet_analiticki()))

    def relativna_pogreska(self, dt):
        greska=(abs(self.domet_analiticki()-self.range(dt))/self.domet_analiticki())*100
        return greska

        