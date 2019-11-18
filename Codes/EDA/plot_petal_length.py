import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np 

#petal length in a list (cm)
versi_color_petal = [4.7, 4.5, 4.9, 4.0,  4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4.0,  4.7, 3.6, 4.4, 4.5, 4.1,
     4.5, 3.9, 4.8, 4.0,  4.9, 4.7, 4.3, 4.4, 4.8, 5.0,  4.5, 3.5, 3.8, 3.7, 3.9, 5.1, 4.5, 4.5,
     4.7, 4.4, 4.1, 4.0,  4.4, 4.6, 4.0,  3.3, 4.2, 4.2, 4.2, 4.3, 3.0,  4.1]

n_data = len(versi_color_petal)
n_bins = np.sqrt(n_data)
n_bins = int(n_bins)

sb.set()
plt.hist(versi_color_petal, bins = n_bins)
plt.xlabel('petal length (cm)')
plt.ylabel('count')

plt.show()

