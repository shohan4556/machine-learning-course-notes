import numpy as np 
import matplotlib.pyplot as plt

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
    versi_color_petal = [4.7, 4.5, 4.9, 4.0,  4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4.0,  4.7, 3.6, 4.4, 4.5, 4.1,
     4.5, 3.9, 4.8, 4.0,  4.9, 4.7, 4.3, 4.4, 4.8, 5.0,  4.5, 3.5, 3.8, 3.7, 3.9, 5.1, 4.5, 4.5,
     4.7, 4.4, 4.1, 4.0,  4.4, 4.6, 4.0,  3.3, 4.2, 4.2, 4.2, 4.3, 3.0,  4.1]
    
    x_vers, y_vers = ecdf(versi_color_petal)
    plt.plot(x_vers,y_vers, marker='.', linestyle = 'none')
    # can multiple ecdf on the same plot and compare

    plt.xlabel('petal length')
    plt.ylabel('ECDF')

    plt.show()


main()