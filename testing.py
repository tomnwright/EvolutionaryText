import string
from evolution import *
from tools import *



import matplotlib.pyplot as plt

def makeGraph(title, xData, yData, xLabel, yLabel):
    fig, ax = plt.subplots()
    ax.plot(xData, yData, 'o', markersize=3)

    ax.set(xlabel=xLabel, ylabel=yLabel,
        title=title)
    ax.grid()

    fig.savefig("test.png")
    plt.show()



test = 'Methinks it is a weasel'

pool = Pool(string.ascii_letters + ' ')
evolver = Evolver(pool, test)

import numpy
tests = [0.005,] + list(numpy.arange(0.01, 0.25, 0.005))
x=[]
y = []
for i in tests:
    for repeat in range(4):
        gens = evolver.evolve(mProb = i)
        x.append(i)
        y.append(gens)

makeGraph('asf', x, y,'sdfx','asdy')

