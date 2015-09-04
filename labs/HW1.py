import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,10,.1)
x = np.cos(2*np.pi*t)
y = np.exp(t*(-.9))*np.cos(2*np.pi*t)

plt.plot(t, y)
plt.show()