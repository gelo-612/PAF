import matplotlib.pyplot as plt

def nacrtaj_graf(x1, y1, x2, y2):
    # izračunaj jednadžbu pravca
    k = (y2 - y1) / (x2 - x1)
    n = y1 - k*x1
    y=y1-k*x1
    
    
    # nacrtaj točke
    plt.scatter(x1, y1)
    plt.scatter(x2, y2)
    
    # nacrtaj pravac
    x = [x1, x2]
    y = [y1, y2]
    plt.plot(x, y)
    
    # prikaži ili spremi graf
    a=input('ako zelite prikazati graf napisite prikazi,ako zelite spremiti kao pdf napisite pdf-')
    if a=='prikazi':
        plt.show()
    elif a=='pdf':
         plt.savefig("graf.pdf")   
nacrtaj_graf(1, 2, 3, 4)
