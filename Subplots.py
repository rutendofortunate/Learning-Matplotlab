import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x = np.arange(100)

fig, axs = plt.subplots(2,2)

axs[0,0].plot(x, np.sin(x))
axs[0,0].set_title("Sine Wave")

axs[0,1].plot(x, np.sin(x))
axs[0,1].set_title("Cosine Wave")

axs[1,0].plot(x, np.random.random(100))
axs[1,0].set_title("Random Function")

axs[1,1].plot(x, np.log(x))
axs[1,1].set_title("Log Function")
axs[1,1].set_xlabel("TEST")

fig.suptitle("Four Plots")

plt.tight_layout()
plt.savefig("fourplots.png", dpi=300, transparent =True, bbox_inches="tight", pad_inches =0.2)
plt.show()