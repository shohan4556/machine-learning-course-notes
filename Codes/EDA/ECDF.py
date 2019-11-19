import numpy as np 
import matplotlib.pylot as plt

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

def main():    
    x_vers, y_vers = ecdf(versicolor_petal_length)
    plt.plot(x_vers,y_vers, marker='.', linestyle = 'none')

    plt.xlabel('petal length')
    plt.ylabel('ECDF')

    plt.show()


main()