# -*- coding: utf-8 -*-
import matplotlib

print(matplotlib.__version__)

# 1.5.1



import numpy as np

from scipy.stats import multivariate_normal



#for plotting

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


def main():

    m = 2 #dimension

    mean = np.zeros(m)

    sigma = np.eye(m)

    N = 1000

    x1 = np.linspace(-5, 5, N)

    x2 = np.linspace(-5, 5, N)



    X1, X2 = np.meshgrid(x1, x2)

    X = np.c_[np.ravel(X1), np.ravel(X2)]



    Y_plot = multivariate_normal.pdf(x=X, mean=mean, cov=sigma)
    #print(Y_plot.shape())

    Y_plot = Y_plot.reshape(X1.shape)

    #print(Y_plot.shape())


    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X1, X2, Y_plot, cmap='bwr', linewidth=0)

    fig.colorbar(surf)

    ax.set_title("Surface Plot")

    fig.show()

    raw_input()

    # X1.shape : (1000, 1000)

    # X2.shape : (1000, 1000)

    # Y_plot.shape : (1000, 1000)




if __name__ == "__main__":
    main()
