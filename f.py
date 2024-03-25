import numpy as np
import matplotlib.pyplot as plt


def f(r, n, x):
    one_over_w = r*(1/n**2-1/x**2)
    w = 1/one_over_w
    nm_w = w*10**9
    return nm_w


def g(r, n):
    one_over_w = r*(1/n**2)
    w = 1/one_over_w
    nm_w = w*10**9
    return nm_w


def get_plot(r, n, title, color):
    x = np.linspace(n+1, 11, 100000)
    plt.plot(x, f(r, n, x), color=color)

    x = [i for i in range(n+1, 12)]
    fs = [f(r, n, i) for i in x]
    plt.scatter(x, fs, color=color, label=title)

    plt.hlines(g(r, n), n+1, 11, color=color, linestyle="dashed")

    if title != "":
        with open("lines.txt", "a") as file:
            file.write(f"{title}\n")
            for i in fs:
                file.write(f"{x[fs.index(i)]} {i}\n")
            file.write(f"i {g(r, n)}\n\n")


def get_subplot(r, n, title):
    plt.subplot(3, 2, n)

    get_plot(r, n, "", "blue")

    plt.xlim(n+1, 11)
    plt.ylim(g(r, n), f(r, n, n+1)-1)
    plt.xticks(range(n+1, 12))

    plt.title(title)
    plt.xlabel("Energy Level")
    plt.ylabel("λ (nm)")

