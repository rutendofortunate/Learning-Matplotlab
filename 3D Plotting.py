import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

ax = plt.axes(projection="3d")

#x = np.random.random(100)
#y = np.random.random(100)
#z = np.random.random(100)

#x = np.arange(0,50,0.1)
#y = np.sin(x)
#z = np.cos(x)

#x = np.arange(0,50,0.1)
#y = np.arange(0,50,0.1)
#z = np.cos(x+y)

x = np.arange(0,50,0.1)
y = np.arange(0,50,0.1)

X, Y =np.meshgrid(x,y)

Z = np.sin(X) * np.cos(Y)

#for the last 3D example you will need to use the plot_surface
ax.plot_surface(X, Y, Z, cmap="Spectral")

#ax.scatter(x,y,z)
ax.set_title("3D PLOT")
ax.set_xlabel("test")

#this is for the last 3D example
ax.view_init(azim=0, elev=90)

plt.show()