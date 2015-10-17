import math

import matplotlib.pyplot as plt
import numpy as num


# self, mu, noiseSTD, tvec = argv

tvec = num.linspace(0, 10, 1000)
mu = 1
noiseSTD = 0.1

# Parameter initialization
xzero = 1
yzero = -1
Dtfac = 10 ** 2
Dt = (tvec[1] - tvec[0]) / Dtfac
N = int(tvec[len(tvec) - 1] / Dt)

# Generate random seed and values
num.random.seed(100)
xdW = math.sqrt(Dt) * num.random.randn(N)
ydW = math.sqrt(Dt) * num.random.randn(N)

# Initialize the variables
xdet = num.zeros(N);
xdet[0] = xzero
ydet = num.zeros(N);
ydet[0] = yzero
xsto = num.zeros(N);
xsto[0] = xzero
ysto = num.zeros(N);
ysto[0] = yzero

for ind in range(1, N):
    xdet[ind] = xdet[ind - 1] + Dt * (
    mu * xdet[ind - 1] - 2 * math.pi * ydet[ind - 1] - xdet[ind - 1] * (xdet[ind - 1] ** 2 + ydet[ind - 1] ** 2))
    ydet[ind] = ydet[ind - 1] + Dt * (
    2 * math.pi * xdet[ind - 1] + mu * ydet[ind - 1] - ydet[ind - 1] * (xdet[ind - 1] ** 2 + ydet[ind - 1] ** 2))

    xsto[ind] = xsto[ind - 1] + Dt * (mu * xsto[ind - 1] - 2 * math.pi * ysto[ind - 1] - xsto[ind - 1] * (
    xsto[ind - 1] ** 2 + ysto[ind - 1] ** 2)) + noiseSTD * xdW[ind]
    ysto[ind] = ysto[ind - 1] + Dt * (2 * math.pi * xsto[ind - 1] + mu * ysto[ind - 1] - ysto[ind - 1] * (
    xsto[ind - 1] ** 2 + ysto[ind - 1] ** 2)) + noiseSTD * ydW[ind]

plt.plot(xsto)
plt.show()
