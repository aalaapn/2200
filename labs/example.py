"""Examples illustrating the use of plt.subplots().

This function creates a figure and a grid of subplots with a single call, while
providing reasonable control over how the individual plots are created.  For
very refined tuning of subplot creation, you can still use add_subplot()
directly on a new figure.
"""

import matplotlib.pyplot as plt
import numpy as np

# Simple data to display in various forms
t=np.arange(0,10)
x = np.cos(2*np.pi*t)
y = np.exp(t*(-.9))*np.cos(2*np.pi*t)

plt.close('all')

# Just a figure and one subplot
f, (ax1, ax2) = plt.subplots(1,2,sharey=False)
ax1.plot(t, y)
ax2.plot(t,x)
ax1.set_title('C.1.')
ax2.set_title('C.2.')


plt.show()