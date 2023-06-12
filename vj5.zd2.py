import calculus as cal
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def fx(x):
    return 2*x**2+3

anal_rj = []

t = sp.Symbol('t')
f = 2*t**2 + 3
dgr = 0
ggr = 1
F = sp.integrate(f, (t, dgr, ggr)) 
g = float(F)
anal_rj.append(g)

i = cal.integ(a=0., b=1., n=50.)
granicni_integrali = i.integr1(f=fx)
print('test')
print('Gornja granica : '.format(granicni_integrali[1]))
print('Donja granica : '.format(granicni_integrali[0]))

tr = i.integr2(f=fx)
print('Kroz trap. formulu integral je : {}.'.format(tr))
gornja=[]
donja=[]
trap=[]
n=np.linspace(15,100,25)
for l in n:
    i = cal.integ(a=0., b=1., n=int(l))
    c=i.integr1(f=fx)
    gornja.append(c[0])
    donja.append(c[1])
    t=i.integr2(f=fx)
    trap.append(t)
plt.plot(n, donja, 'o',color='red' ,label="Donja granica")
plt.plot(n, gornja, 'o',color='blue' ,label="Gornja granica")
plt.plot(n, trap, 'o',color='black' ,label="Trapezna formula")
plt.plot(n, [anal_rj[0]]*len(n), '-', color='magenta', label="Analiticko rjesenje")
plt.title('Upotreba integracije')
plt.xlabel('Broj koraka N')
plt.ylabel('integracija')
plt.legend()
plt.show()