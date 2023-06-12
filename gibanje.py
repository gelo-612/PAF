import particle as prc
import math
import numpy as np
import matplotlib.pyplot as plt
p1=prc.Particle(60,40,[0,0])
p1.range(0.01)
print(p1.domet_analiticki())
print(p1.odstupanje(0.01))
