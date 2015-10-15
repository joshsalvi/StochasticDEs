import numpy as np
import matplotlib.pyplot as plt
from time import time

np.random.seed(4242)

T = 1
N = 500
dt = float(T)/N
t = np.linspace(0, T, N+1)

dW = np.sqrt(dt)*np.random.randn(N)
W = np.cumsum(dW);
W = np.insert(W, 0, 0)

plt.plot(t, W)
plt.xlabel(r'$t$', fontsize=16); plt.ylabel(r'$W(t)$', fontsize=16, rotation=0)
plt.title('A Brownian path')
plt.show()
