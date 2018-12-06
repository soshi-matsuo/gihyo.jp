import matplotlib.pyplot as plt
import numpy as np
import math


def poisson(lambd, x):
    return (np.exp(-lambd)) * (lambd ** x) / (math.factorial(x))

N = 8
L = []
score_mean = 0.7

L.append([poisson(score_mean, k) for k in range(N + 1)])

for prob in L:
    plt.plot(range(N + 1), prob, 'r')

ax = plt.axes()
ax.set_xlim(0, N)
ax.set_ylim(-0.01, 0.5)
plt.title('Soccer Score')
plt.xlabel('Score')
plt.ylabel('Probability')
plt.grid(True)

plt.show()