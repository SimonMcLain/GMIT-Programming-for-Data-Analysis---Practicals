# Simon McLain 2018-09-01
# Week 2 Lectures intro to pyplot in matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0 
noise = np.random.normal(0.0, 1.0, len(x))

plt.plot(x, y + noise, 'r.', label="Actual")
plt.plot(x, y, 'b-', label="Model")
plt.title("Simple Plot")
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend()

plt.show()


