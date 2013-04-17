import pixmap
import math

x, y = 30, 30
grid = [[0 for i in range(x)] for i in range(y)]

def d(xi, yi, xj, yj):
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

grid = [(lambda x:[[i] * 3 for i in x])(i) for i in grid]
pixmap.save(grid, 'visualization.ppm')
