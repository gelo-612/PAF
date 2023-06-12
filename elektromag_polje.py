import math
import numpy as np
import matplotlib.pyplot as plt

class elektromag_polje:
    def __init__(self):
        self.lista_x = []
        self.lista_y = []
        self.lista_z = []


    def init(self, x0, y0, z0, v0, masa, naboj, elektricno_polje, magnetno_polje, dt=0.01):
        self.v = v0
        self.m = masa
        self.q = naboj
        self.E = elektricno_polje
        self.B = magnetno_polje
        self.dt = dt

        self.lista_x.append(x0)
        self.lista_y.append(y0)
        self.lista_z.append(z0)

        self.a = np.array((0,0,0))



    def __move(self, i):

        self.a = (self.q)*(self.E + np.cross(self.v,self.B)/self.m)
        self.v = self.v + self.a*self.dt

        
        self.lista_x.append(self.lista_x[i-1] + self.v[0]*self.dt)
        self.lista_y.append(self.lista_y[i-1] + self.v[1]*self.dt)
        self.lista_z.append(self.lista_z[i-1] + self.v[2]*self.dt)


    def putanja(self, T=30):

        dT = int(T/0.01)
        el = 0

        while el < dT:
            self.__move(el)
            el += 1
        return self.lista_x, self.lista_y, self.lista_z