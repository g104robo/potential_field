# -*- coding: utf-8 -*-

import numpy as np


x_att = [1.0, 1.0]
x_rep = [2.0, 1.0]

C_ATT = 1.0
L_ATT = 1.0

C_REP = 1.0
L_REP = 1.0

def u_att (c_att, l_att, x):
    return c_att*(1-np.exp(-((x[0]-x_att[0])**2 + (x[1]-x_att[1])**2)/l_att))

def u_rep (c_rep, l_rep, x):
    return c_rep*np.exp(-((x[0]-x_rep[0])**2 + (x[1]-x_rep[1])**2)/l_rep)

def main():
    x = [0.0, 0.0]
    print (u_att(C_ATT, L_ATT, x))
    print (u_rep(C_REP, L_REP, x))

N = 1000
x1 = np.linspace(-5, 5, N)
x2 = np.linspace(-5, 5, N)

X1, X2 = np.meshgrid(x1, x2)
X = np.c_[np.ravel(X1), np.ravel(X2)]

Y_plot = multivariate_normal.pdf(x=X, mean=mean, cov=sigma)
Y_plot = Y_plot.reshape(X1.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X1, X2, Y_plot, cmap='bwr', linewidth=0)
fig.colorbar(surf)
ax.set_title("Surface Plot")
fig.show()

if __name__ == "__main__":
    main()
