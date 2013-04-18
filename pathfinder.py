import pixmap
import math

w, h = 1000, 1000
grid = [[0 for i in range(w)] for i in range(h)]

def d(xi, yi, xj, yj):
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

def p(x, y, r=10):
    for j in range(w):
        for i in range(h):
            grid[i][j] = grid[i][j] + (lambda x: (r-x) if x <= r else 0)(d(x, y, i, j))

ps = [(0, 0), (20, 20), (500, 500), (750, 750)]
for i in range(len(ps)):
    p(*ps[i], r=d(*ps[i] + ps[i-1])) if i > 1 else p(*ps[i])

grid = [(lambda x:[[int(i*100)] * 3 for i in x])(i) for i in grid]
pixmap.save(grid, 'visualization.ppm')
