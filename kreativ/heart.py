from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML

def corazon_3d(x, y, z):
    a = (x**2 + (9/4)*(y**2) + z**2 - 1)**3
    b = x**2*z**3
    c = (9/88)*(y**2)*(z**3)
    return a - b - c

bbox = (-1.5, 1.5)

xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')

A = np.linspace(xmin, xmax, 100)
B = np.linspace(xmin, xmax, 50)
A1, A2 = np.meshgrid(A, A)

for z in B:
    X, Y = A1, A2
    Z = corazon_3d(X, Y, z)
    cset = ax.contour(X, Y, Z + z, zdir='z', colors=('red'))

for y in B:
    X, Z = A1, A2
    Y = corazon_3d(X, y, Z)
    cset = ax.contour(X, Y + y, Z, [y], zdir='y', colors=('red'))

for x in B:
    Y, Z = A1, A2
    X = corazon_3d(x, Y, Z)
    cset = ax.contour(X + x, Y, Z, [x], zdir='x', colors=('red'))

ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.set_zlim3d(zmin, zmax)
ax.set_xlim3d(xmin, xmax)
ax.set_ylim3d(ymin, ymax)

def animate(i):
    ax.view_init(elev=10., azim=i)
    return fig,

plt.show()
