import matplotlib.pyplot as plt
import numpy as np
import math

# compute combination of success pattern
def combi(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

# compute binomial distribution
def binomial_dist(n, x, p):
    com = combi(n, x)
    return com * (p ** x) * ((1-p) ** (n - x))

p = 0.5 # probability of bernoulli trial
L = []
trial_count = (10, 20, 30, 40, 50)
colors = ['r', 'g', 'b', 'c', 'y']

for n in trial_count:
    L.append([binomial_dist(n, x, p) for x in range(n)])

for prob, color in zip(L, colors):
    plt.plot(prob, color)

# n回のベルヌーイ試行中にx回成功する確率の分布

ax = plt.axes()
ax.set_xlim(0,50)
ax.set_ylim(-0.05, 0.3)

plt.title('Binomial Distribution P={}'.format(p))
plt.xlabel('number of Trial')
plt.ylabel('Probability')
plt.legend([str(n) for n in trial_count])
plt.show()