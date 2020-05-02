quad = list(map(int, input()))

zoom_level = len(quad)
coords = [(0, 0), (1, 0),
          (0, 1), (1, 1)]
x_y = [0, 0]
for q in quad:
    x_y = [p * 2 for p in x_y]
    x_y = [p + mod for p, mod in zip(x_y, coords[q])]
print(zoom_level, *x_y)