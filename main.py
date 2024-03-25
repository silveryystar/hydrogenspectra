import matplotlib.pyplot as plt
from f import get_plot, get_subplot

ryberg_constant = 1.0973731568160*10**7
proton_mass = 1.67262192369*10**-27
electron_mass = 9.1093837015*10**-31

r = ryberg_constant*proton_mass/(proton_mass+electron_mass)

titles = ["Lyman (n=1)", "Balmer (n=2)", "Paschen (n=3)", "Brackett (n=4)", "Pfund (n=5)", "Humphreys (n=6)"]
colors = ["red", "orange", "green", "blue", "purple", "black"]

for i in range(1, 7):
    get_plot(r, i, titles[i-1], colors[i-1])

plt.xlim(2, 11)
plt.yscale("log")

plt.title("Hydrogen Spectral Series")
plt.xlabel("Energy Level")
plt.ylabel("λ (nm)")
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()

for i in range(1, 7):
    get_subplot(r, i, titles[i-1])

plt.suptitle("Hydrogen Spectral Series")
plt.tight_layout()
plt.show()
