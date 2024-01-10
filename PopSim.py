import matplotlib.pyplot as plt
import pandas as pd 
from colorama import Fore, Style # Farger i konsollen

# Definerer 4 Subplots og fjerner en av dem pga vi bare trenger 3 grafer
fig, ((ax1, _), (ax2, ax3)) = plt.subplots(2,2, sharex=True)
_.axis('off')

# Finner hvor mange som er født dette året og fjerner tomme verdier
bpy = [x for x in pd.read_csv("./births-per-year.csv")["Births"].tolist() if str(x)!="nan"]
# Gjør det samme men finner estimerte verdier for fremtiden (dette er data fra 2021 så 2022+ regnes som fremtiden)
ebpy = [x for x in pd.read_csv("./births-per-year.csv")["Estimate"].tolist() if str(x)!="nan"]
# Finner hvor mange som er dør dette året og fjerner tomme verdier
dpy = [x for x in pd.read_csv("./deaths-per-year.csv")["Deaths"].tolist() if str(x)!="nan"]
# Gjør det samme men finner estimerte verdier for fremtiden
edpy = [x for x in pd.read_csv("./deaths-per-year.csv")["Estimate"].tolist() if str(x)!="nan"]
# Lager Akse navn og titler på grafene
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

# Definerer start populasjonen (konstantleddet) fra 1950
populasjon = 2532229000

# Definerer 4 lister vi bruker til informasjon
xv, yv, xv2, yv2 = ([],[],[],[])

# Looper gjennom fødsler og døde og legger dem til i listene
for i in range(len(bpy)):
    xv.append(i+1950)
    xv2.append(i+1950)
    yv.append(bpy[i])
    yv2.append(dpy[i])
# Plotter fødsler og døde i blå farge
ax2.plot(xv, yv, color="b")
ax3.plot(xv2, yv2, color="b")

# Resetter de 4 første listene
xv, xv2, yv, yv2 = ([],[],[],[])
# Lopper gjennom igen bare med estimerte verdier
for i in range(len(ebpy)):
    xv.append(i+2022)
    xv2.append(i+2022)
    yv.append(ebpy[i])
    yv2.append(edpy[i])
# Plotter de estimerte verdiene
ax2.plot(xv, yv, color="r")
ax3.plot(xv2, yv2, color="r")

# Resetter listene
xv, xv2, yv, yv2 = ([],[],[],[])

# Looper gjennom alle verdier i bpy
for i in range(len(bpy)):
    # Setter in verdier i listene
    xv.append(i+1950) # Hær plusser jeg på 1950 fordi jeg vill at grafen skal starte i 1950
    yv.append(populasjon)
    
    # Populasjonen blir endret utifra hvor mange som blir født og hvor mange som dør
    populasjon+=bpy[i]
    populasjon-=dpy[i]
    print(f"{Fore.GREEN}År: {i+1950}, {Fore.YELLOW}Populasjon: {populasjon}, {Fore.BLUE}Født dette året: {bpy[i]}, {Fore.RED}Døde dette året: {dpy[i]}{Style.RESET_ALL}")
# Plotter verdier for x i [1950 til 2021] (blå farge)
ax1.plot(xv, yv, color="b")

print(populasjon/2)
edpy[0]=populasjon/2
# Samme som forgje lopp bare i fremtiden
for i in range(len(ebpy)):
    xv2.append(i+2022)
    yv2.append(populasjon)

    populasjon+=ebpy[i]
    populasjon-=edpy[i]
    print(f"{Fore.GREEN}År: {xv2[i]}, {Fore.YELLOW}Populasjon: {populasjon}, {Fore.BLUE}Født dette året: {ebpy[i]}, {Fore.RED}Døde dette året: {edpy[i]}{Style.RESET_ALL}")

# Plotter verdier for x i [2022 til 2100] (rød farge)
ax1.plot(xv2, yv2, color="r")

# Viser grafene
fig.show()
plt.show()