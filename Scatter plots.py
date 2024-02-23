import numpy as np
import matplotlib.pyplot as plt

X_data = np.random.random(50)*100
y_data = np.random.random(50)*100

plt.scatter(X_data, y_data, c="red", marker='*', s=150, alpha=0.3)

#print(X_data)

plt.show()