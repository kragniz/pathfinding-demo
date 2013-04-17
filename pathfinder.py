import pixmap

x, y = 30, 30
grid = [[0 for i in range(x)] for i in range(y)]
grid = [(lambda x:[[i] * 3 for i in x])(i) for i in grid]
pixmap.save(grid, 'visualization.ppm')
