import math
import matplotlib.pyplot as plt
import numpy as np
import particle as prc
dt_lista = []
rel_gr = []
p1=prc.Particle(10,60,[0,0])

for i in range(0, 100):
    dt = i/1000
    dt_lista.append(dt)
    rel_gr.append(p1.relativna_pogreska(dt))
    
    

plt.plot(dt_lista, rel_gr)    
plt.show()




