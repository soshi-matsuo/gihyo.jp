import matplotlib

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

# make imitation data of height
sample = 1000
mu, sigma = 170, 5
data = np.random.normal(mu, sigma, sample)

# plot histgram
plt.hist(data, normed=1)

plt.title('Histgram of Height: mu={},sigma={}'.format(mu, sigma))
plt.xlabel('Height')
plt.ylabel('Probability')
plt.grid(True)

plt.show()