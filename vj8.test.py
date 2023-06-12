import numpy as np
import elektromag_polje as emf
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


p1 = emf.elektromag_polje() #elektron
p2 = emf.elektromag_polje() #pozitron


p1.init(0,0,0,np.array((0.1,0.1,0.1)),1,-1,np.array((0,0,0)),np.array((0,0,1)))
p2.init(0,0,0,np.array((0.1,0.1,0.1)),1,1,np.array((0,0,0)),np.array((0,0,1)))

x1, y1, z1 = p1.putanja(20)
x2, y2, z2 = p2.putanja(20)

fig = plt.figure()


ax = plt.axes(projection="3d")
ax.plot3D(x1, y1, z1, c="r", label="elektron")
ax.plot3D(x2, y2, z2, c="b", label="pozitron")


plt.legend(["elektron", "pozitron"])

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z', fontsize=12)

plt.show()
