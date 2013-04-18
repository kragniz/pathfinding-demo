import pixmap
import math

w, h = 100, 100
grid = [[0 for i in range(w)] for i in range(h)]

def d(xi, yi, xj, yj):
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

def p(x, y, r=10):
    for j in range(w):
        for i in range(h):
            grid[i][j] = grid[i][j] + (lambda x: (r-x) if x <= r else 0)(d(x, y, i, j))
p(50, 50, r=20)
p(50, 39)
grid = [(lambda x:[[int(i*2000)] * 3 for i in x])(i) for i in grid]
pixmap.save(grid, 'visualization.ppm')
