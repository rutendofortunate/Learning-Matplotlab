import numpy as np
import matplotlib.pyplot as plt

langs =["C++", "C#", "Python", "Java", "Go"]
votes=[24,6,50,14,17]
explodes = [0,0.2,0,0,0]

plt.pie(votes, labels = None, explode = explodes,
        autopct = "%.2f%%", pctdistance=0.5,startangle=90 )
plt.legend(labels=langs)
plt.show()