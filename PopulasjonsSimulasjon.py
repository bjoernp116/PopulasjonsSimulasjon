import matplotlib.pyplot as plt
from colorama import Style, Fore
import pandas as pd

def importer_data():
    bpy = [x for x in pd.read_csv("./births-per-year.csv")["Births"].tolist() if str(x)!="nan"]
    ebpy = [x for x in pd.read_csv("./births-per-year.csv")["Estimate"].tolist() if str(x)!="nan"]
    dpy = [x for x in pd.read_csv("./deaths-per-year.csv")["Deaths"].tolist() if str(x)!="nan"]
    edpy = [x for x in pd.read_csv("./deaths-per-year.csv")["Estimate"].tolist() if str(x)!="nan"]
    return (bpy, ebpy, dpy, edpy)



def plot_populasjon(bpy, dpy, xs, ys, farge):
    populasjon = ys
    (arrx, arry) = ([],[])
    for i in range(len(bpy)):
        populasjon += bpy[i]
        populasjon -= dpy[i]
        print(f"{i}: {Fore.GREEN}År: {i+xs}, {Fore.YELLOW}Populasjon: {populasjon}, {Fore.BLUE}Født dette året: {bpy[i]}, {Fore.RED}Døde dette året: {dpy[i]}{Style.RESET_ALL}")
        
    plt.plot(arrx, arry, color=farge)
def main():
    (bpy, ebpy, dpy, edpy) = importer_data()
    plot_populasjon(bpy, dpy, 1950, 2575523720, 'r')

main()


