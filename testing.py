import string
from evolution import *
from tools import *

from writetest import Writer

# import matplotlib.pyplot as plt

# def makeGraph(title, xData, yData, xLabel, yLabel):
#     fig, ax = plt.subplots()
#     ax.plot(xData, yData, 'o', markersize=3)

#     ax.set(xlabel=xLabel, ylabel=yLabel,
#         title=title)
#     ax.grid()

#     fig.savefig("test.png")
#     plt.show()

def scatter3D(title, xData, yData, zData, xLabel, yLabel, zLabel):
    # This import registers the 3D projection, but is otherwise unused.
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
    import matplotlib.pyplot as plt
    import time

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #n = 100

    # For each set of style and range settings, plot n random points in the box
    # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
    
    ax.scatter(xData, yData, zData, c = zData, cmap = 'viridis')

    ax.set(xlabel=xLabel, ylabel=yLabel, zlabel = zLabel, title = title)

    timenow = time.time()
    fig.savefig(f"test{timenow}.png")

    plt.show()

def randfloat(minimum, maximum, resolution):
    
    lower = int(minimum / resolution)
    upper = int(maximum / resolution)
    
    return resolution * random.randint(lower, upper)

# test = 'Methinks it is a weasel'

# pool = Pool(string.ascii_letters + ' ')
# evolver = Evolver(pool, test)

# import numpy

# xRange = (0.001,0.3)
# yRange = (1,25)

# x,y,z = [],[],[]

# writer = Writer()

# for i in range(3000):
#     xS = randfloat(*xRange, 0.01)
#     yS = randfloat(*yRange, 1)

#     #print(xS, yS)

#     gens = evolver.evolve(mProb = xS, mLim = yS)
    
#     writer.write(xS, yS, gens)


from writetest import Reader
reader = Reader("main.txt")
x,y,z = reader.getdata()


scatter3D(
    'Effect of Mutation Probability and Mutation Range on Max Generation',
    x,y,z,
    'Mutation Probability',
    'Mutation Range',
    'Generations to Target')




