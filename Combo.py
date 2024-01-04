import numpy as np
import matplotlib
from matplotlib import pyplot as plt

beat = np.array([180, 33, 46, 76, 88, 222])
explode = np.zeros(len(beat))
explode[beat.argmax()] = 0.1
plt.pie(beat, labels=beat, explode=explode)
plt.show()