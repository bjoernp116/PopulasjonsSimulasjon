import matplotlib.pyplot as plt
from colorama import Style, Fore
import pandas as pd

# Importer data fra csv filer
def importer_data():
    bpy = [x for x in pd.read_csv("./Data/births-per-year.csv")["Births"].tolist() if str(x)!="nan"]
    ebpy = [x for x in pd.read_csv("./Data/births-per-year.csv")["Estimate"].tolist() if str(x)!="nan"]
    dpy = [x for x in pd.read_csv("./Data/deaths-per-year.csv")["Deaths"].tolist() if str(x)!="nan"]
    edpy = [x for x in pd.read_csv("./Data/deaths-per-year.csv")["Estimate"].tolist() if str(x)!="nan"]
    return (bpy, ebpy, dpy, edpy)

# Inisier de 3 forskjellige aksene og gi dem aksenavn og titteler
def init_plot():
    fig, ((ax1, _), (ax2, ax3)) = plt.subplots(2,2, sharex=True)
    _.axis('off')
    ax1.set_title("Populasjon")
    ax1.set_xlabel("År")
    ax1.set_ylabel("Populasjon (10 milliarder)")
    ax2.set_title("Født per år")
    ax2.set_ylabel("Fødselsrate (100 millioner)")
    ax2.sharey(ax3)
    ax3.set_title("Død per år")
    ax3.set_ylabel("Dødsrate (100 millioner)")
    ax1.grid()
    ax2.grid()
    ax3.grid()
    fig.suptitle("Estimert fremtidig Populasjon i Verden")
    return (fig, (ax1, ax2, ax3))

# Funksjon for å plotte populasjon
def plot_populasjon(akse, bpy, dpy, xs, ys, farge):
    # Konstantleddet er verdenspopulasjonen i 1950
    populasjon = ys
    (arrx, arry) = ([],[])
    # Loop gjennom født og døde per år
    for i in range(len(bpy)):
        # Endre populasjonen med hvor mange som er født og hvor mange som dør
        populasjon += bpy[i]
        populasjon -= dpy[i]
        # Her legger vi til xs for å starte grafen vår i 1950
        arrx.append(i+xs)
        arry.append(populasjon)
        print(f"{i}: {Fore.GREEN}År: {i+xs}, {Fore.YELLOW}Populasjon: {populasjon}, {Fore.BLUE}Født dette året: {bpy[i]}, {Fore.RED}Døde dette året: {dpy[i]}{Style.RESET_ALL}")
    
    # Plot grafen
    akse.plot(arrx, arry, color=farge)
def main():
    # Inisialiser plot
    (fig, (ax1, ax2, ax3)) = init_plot()
    # Importer data
    (bpy, ebpy, dpy, edpy) = importer_data()
    # Plot populasjon fra 1950 med konstantledd på 2575523720 (Verdensbefolking i 1950)
    plot_populasjon(ax1, bpy, dpy, 1950, 2575523720, 'g')
    # Plot estimert populasjon fra 2021 med konstantledd på 8039535724 (Verdensbefolking i 2021)
    plot_populasjon(ax1, ebpy, edpy, 2021, 8039535724.0, 'r')

    # Plot fødte, døde og de estimerte verdiene
    ax2.plot(range(1950, 1950+72), bpy, color='g')
    ax2.plot(range(2021, 2021+79), ebpy, color='r')
    ax3.plot(range(1950, 1950+72), dpy, color='g')
    ax3.plot(range(2021, 2021+79), edpy, color='r')
    fig.show()
    plt.show()
    
main()



