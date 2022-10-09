import math as m
import pygame as pg
import pygame.locals
import numpy as np

points = [(0.1, 0.7), (0, 0.1), (0.6, 0.1)]

a = []
b = []
distx = []

for i in range(2):
    a.append((points[i][1] - points[i + 1][1]) / (points[i][0] - points[i + 1][0]))
    b.append(-a[i] * points[i][0] + points[i][1])

    distx.append(abs(points[i][0] - points[i + 1][0]))

    print(a[i], " * x + ", b[i])
    print(distx[i])

slide_a = []
slide_b = []

curve_points = []
build_a = []
build_b = []

RESOLUTION = 25
for i in np.arange(0, 1, 1 / RESOLUTION):
    slide_a.append(((distx[0] * i, (distx[0] * i) * a[0] + b[0])))
    slide_b.append(((distx[1] * i, (distx[1] * i) * a[1] + b[1])))

for i in range(len(slide_a)):
    build_a.append((slide_a[i][1] - slide_b[-i][1]) / (slide_a[i][0] - slide_b[-i][0]))
    build_b.append(-build_a[-1] * slide_a[i][0] + slide_a[i][1])

for i in range(len(slide_a) - 1):
    x = (build_b[i + 1] - build_b[i]) / (build_a[i] - build_a[i + 1])
    y = x * build_a[i] + build_b[i]

    curve_points.append((x, y))

pg.init()
screen = pg.display.set_mode((800, 600))


e = pg.event.poll()
while(e.type != pg.QUIT):
    e = pg.event.poll()

    for i in range(2):
        pg.draw.line(screen, (255, 255, 255), (points[i][0] * 800, points[i][1] * 600), (points[i + 1][0] * 800, points[i + 1][1] * 600))
    
    for s in slide_a:
        pg.draw.circle(screen, (255, 127, 0), (s[0] * 800, s[1] * 600), 5)

    for s in slide_b:
        pg.draw.circle(screen, (0, 255, 127), (s[0] * 800, s[1] * 600), 5)

    """
    for i in range(len(slide_a)):
        pg.draw.line(screen, (255, 255, 255), (slide_a[i][0] * 800, slide_a[i][1] * 600), (slide_b[-i][0] * 800, slide_b[-i][1] * 600))

    for cp in curve_points:
        pg.draw.circle(screen, (255, 0, 255), (cp[0] * 800, cp[1] * 600), 5)
    """

    for i in range(len(curve_points) - 1):
        pg.draw.line(screen, (0, 127, 255), (curve_points[i][0] * 800, curve_points[i][1] * 600), (curve_points[i + 1][0] * 800, curve_points[i + 1][1] * 600), 3)
    pg.draw.line(screen, (0, 127, 255), (curve_points[1][0] * 800, curve_points[1][1] * 600), (slide_b[-1][0] * 800, slide_b[-1][1] * 600), 3)
    pg.draw.line(screen, (0, 127, 255), (curve_points[-1][0] * 800, curve_points[-1][1] * 600), (slide_a[-1][0] * 800, slide_a[-1][1] * 600), 3)

    pg.display.flip()