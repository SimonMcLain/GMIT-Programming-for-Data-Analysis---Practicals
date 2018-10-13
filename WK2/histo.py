# Simon McLain 2018-10-01
# GMIT Programming for Data Analysis Week 2
# Histograms

import matplotlib.pyplot as plt
import numpy as np

plt.subplot(2, 1, 1)
x = np.random.normal(0.00, 1.0, 10000)
plt.hist(x, bins=20)

plt.subplot(2, 1, 2)
x = np.random.uniform(-3.0, 3.0, 10000)
plt.hist(x, bins=20)

plt.show()

