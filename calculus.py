import numpy as np

class der:
    def __init__(self, a, b, x, dx):
        self.a = a
        self.b = b
        self.x = x
        self.dx = dx
        
    def der1(self, f, m=True):#derivacija sa twopoint i three point metodom
        if m:
            der = (f(self.x)-f(self.x-self.dx))/self.dx
        else:
            der = (f(self.x+self.dx)-f(self.x-self.dx))/(2*self.dx)
        return der
    
    def der2(self, f, m=True):
        tocke_derivacije=[]
        N=np.linspace(self.a,self.b,100)
        for ele in N:
            if m:
                der=(f(ele)-f(ele-self.dx))/self.dx
                tocke_derivacije.append(der)
            else:
                der=(f(ele+self.dx)-f(ele-self.dx))/(2*self.dx)
                tocke_derivacije.append(der)
        return N,tocke_derivacije
    
class integ:
    def __init__(self,a,b,n):
        self.a = a
        self.b = b
        self.n = n
        self.dx = (b - a) / n

    def integr1(self, f):#integracija za gornji i donji integral
        gornja_gran = []
        donja_gran = []
        dx = np.linspace(self.a, self.b, self.n+1)
        N = len(dx)-1
        for i in range(N):
            F_U = f(dx[i+1]) * self.dx
            gornja_gran.append(F_U)
            F_L = f(dx[i]) * self.dx
            donja_gran.append(F_L)
        return sum(gornja_gran), sum(donja_gran)
    
    def integr2(self, f):#integracija pmocu formule za trapezni integral
        num=[]
        dx=np.linspace(self.a, self.b, self.n+1)
        N=len(dx)-1
        for j in range(N):
            trap=(f(dx[j])+f(dx[j+1]))*abs(self.dx)/2
            num.append(trap)
        return sum(num)