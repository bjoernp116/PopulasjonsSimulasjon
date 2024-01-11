import matplotlib.pyplot as plt
from colorama import Style, Fore
import pandas as pd

# Importer data fra csv filer
def importer_data():
    bpy = [x for x in pd.read_csv("./births-per-year.csv")["Births"].tolist() if str(x)!="nan"]
    ebpy = [x for x in pd.read_csv("./births-per-year.csv")["Estimate"].tolist() if str(x)!="nan"]
    dpy = [x for x in pd.read_csv("./deaths-per-year.csv")["Deaths"].tolist() if str(x)!="nan"]
    edpy = [x for x in pd.read_csv("./deaths-per-year.csv")["Estimate"].tolist() if str(x)!="nan"]
    return (bpy+ebpy, dpy+edpy)

# Inisier de 3 forskjellige aksene vi bruker å legg til logiske 
def init_plot():
    fig, ((ax1, _), (ax2, ax3)) = plt.subplots(2,2, sharex=True)
    _.axis('off')
    plt.yscale('log')
    ax1.set_title("Populasjon")
    ax1.set_xlabel("År")
    ax1.set_ylabel("Populasjon (10 milliarder)")
    ax2.set_title("Født per år")
    ax2.set_ylabel("Fødselsrate (100 millioner)")
    
    ax3.set_title("Død per år")
    ax3.set_ylabel("Dødsrate (log base 10 representasjon)")
    ax1.grid()
    ax2.grid()
    ax3.grid()
    fig.suptitle("Estimert fremtidig Populasjon i Verden etter at Thanos knipser (2021)")
    return (fig, (ax1, ax2, ax3))

# Definerer en funksjon som ploter populasjonen
def plot_populasjon(akse, bpy, dpy, xs, ys, farge, knips = -1):
    # konstantledd (populasjonen i 1950)
    populasjon = ys
    (arrx, arry) = ([],[])
    for i in range(len(bpy)):
        # Øk populasjon med hvor mange som er født og fjern døde
        populasjon += bpy[i]
        populasjon -= dpy[i]
        # Hær legger jeg til xs til i for å starte grafen i 1950
        arrx.append(i+xs)
        arry.append(populasjon)
        print(f"{i}: {Fore.GREEN}År: {i+xs}, {Fore.YELLOW}Populasjon: {populasjon}, {Fore.BLUE}Født dette året: {bpy[i]}, {Fore.RED}Døde dette året: {dpy[i]}{Style.RESET_ALL}")
    # Plot grafen
    akse.plot(arrx, arry, color=farge)
    return populasjon

# Hoved funksjon
def main():
    # Inistialiser plottet med akse navn
    (fig, (ax1, ax2, ax3)) = init_plot()
    # Importer data (bpy = Født per år)(dpy = Død per år)
    (bpy, dpy) = importer_data()

    # Plot populasjonen opp til 2021 i farge grønn med startledd på 2575523720 (Verdenspopulasjon i 1950)
    populasjon = plot_populasjon(ax1, bpy[:71], dpy[:71], 1950, 2575523720, 'g')
    # Plot populasjon fra 2021 og oppover med startledd på halvparten av det den var i 2021
    plot_populasjon(ax1, bpy[20:], dpy[20:], 2021, populasjon/2, 'r')
    # Halvparten av populasjonen døde i 2021
    dpy[71] = populasjon/2
    # Plot Døde per år og Fødte per år
    ax3.plot(range(1950, 1950+71), dpy[:71], color='g')
    ax3.plot(range(2021, 2021+80), dpy[71:], color='r')
    ax2.plot(range(1950, 1950+71), bpy[:71], color='g')
    # Pga vi var halvparten av det vi var i 2021 i 1970 kan vi estimere at populasjonen kommer til å øke med lik vekst fremover
    ax2.plot(range(2021, 2021+131), bpy[20:], color='r')
    
    fig.show()
    plt.show()
main()



