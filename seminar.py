import matplotlib.pyplot as plt
import math

def provjeri_položaj_točke(x_tocke, y_tocke, x_ishodiste, y_ishodiste, radijus, ime_slike=None):
    udaljenost = math.sqrt((x_tocke-x_ishodiste)**2 + (y_tocke- y_ishodiste)**2) 

    fig, ax = plt.subplots()

    # Crta kružnicu
    circle = plt.Circle((x_ishodiste, y_ishodiste), radijus, edgecolor='black', facecolor='none')
    ax.add_patch(circle)

    # Crta točku
    ax.plot(x_tocke, y_tocke, 'ro')

    # Provjerava položaj točke
    if udaljenost < radijus:
        položaj = "unutar"
    elif udaljenost == radijus:
        položaj = "točno na"
    elif udaljenost > radijus:
        položaj = "izvan"

    # Ispisuje rezultat
    rezultat = f"Točka se nalazi {položaj} kružnice. Udaljenost točke od  kružnice: {udaljenost - radijus}"
    print(rezultat)

    # Prikazuje ili sprema sliku
    if ime_slike:
        plt.savefig(ime_slike)
    else:
        plt.show()


# Testiranje funkcije
provjeri_položaj_točke(2, 3, 0, 0, 5, "kružnica.png")
provjeri_položaj_točke(6, 8, 0, 0, 5)
provjeri_položaj_točke(3, 4, 0, 0, 5, "kružnica2.png")
provjeri_položaj_točke(-2, -3, 0, 0, 5)
