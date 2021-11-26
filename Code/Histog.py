import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 50, 20
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, 10, r'$\mu=100,\ \sigma=15$')
plt.xlim(0, 160)
plt.ylim(0, 0.3)
plt.grid(True)
#plt.show()



from matplotlib import pyplot as plt
import numpy as np
fig,ax = plt.subplots(1,1)
a = np.array([1.5,2])
ax.hist(a, bins = [0,1,2])
ax.set_title("histogram of result")
ax.set_xticks([0,1,2])
ax.set_xlabel('marks')
ax.set_ylabel('no. of students')
plt.show()