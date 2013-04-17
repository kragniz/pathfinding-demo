import pixmap

x, y = 30, 30
grid = [[[32768] * 3 for i in range(x)] for i in range(y)]
pixmap.save(grid, 'visualization.ppm')
