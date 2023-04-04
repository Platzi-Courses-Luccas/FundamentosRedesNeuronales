import numpy as np
import matplotlib.pyplot as plt

def sigmoid(a):
    return 1/(1+np.exp(-a))

def step(a):
    return 1 if a>=0 else 0

x = np.linspace(10,-10,100)

# plt.plot(x,sigmoid(x))
# plt.show()

y = step(x)
plt.plot(x,y)
plt.show()