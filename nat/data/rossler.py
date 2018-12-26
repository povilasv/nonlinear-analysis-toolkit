##This is a simple code to solve Rossler equation system in python and plot solutions.
##Made by Hector Corte-Leon leo_corte@yahoo.es on 23/02/2013
##The numerical method used is first order forward Euler method.

#############################################

# Taken from https://thebrickinthesky.wordpress.com/2013/02/23/maths-with-python-2-rossler-system/
# Edited to suite API of this pacakge.

import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy import linspace, zeros


# We define a function which is going to be the recursive function.
def num_rossler(x_n, y_n, z_n, h, a, b, c):
    x_n1 = x_n + h * (-y_n - z_n)
    y_n1 = y_n + h * (x_n + a * y_n)
    z_n1 = z_n + h * (b + z_n * (x_n - c))
    return x_n1, y_n1, z_n1


# TODO: params
def rossler_system(a=0.1, b=0.2, c=5.7, t_ini=0, t_fin=16 * math.pi, h=0.01, length=None, plot=False):
    """

    :param a:
    :param b:
    :param c:
    :param t_ini:
    :param t_fin:
    :param h:
    :param length: number of triples x,y,z. Defaults to ?
    :param plot: True to plot the time series. Defaults to False.

    :return:
    """
    numsteps = length
    if length is None:
        numsteps = int((t_fin - t_ini) / h)

    # using this parameters we build the time.
    t = linspace(t_ini, t_fin, numsteps)
    # And the vectors for the solutions
    x = zeros(numsteps)
    y = zeros(numsteps)
    z = zeros(numsteps)

    # We set the initial conditions
    x[0] = 0
    y[0] = 0
    z[0] = 0

    # This is the main loop where we use the recursive system to obtain the solution
    for k in range(x.size - 1):
        # We use the previous point to generate the new point using the recursion
        [x[k + 1], y[k + 1], z[k + 1]] = num_rossler(x[k], y[k], z[k], t[k + 1] - t[k], a, b, c)

    # Now that we have the solution in vectors t,x,y,z is time to plot them.

    # We create a figure and 4 axes on it. 3 of the axes are going to be 2D and the fourth one is a 3D plot.
    if plot:
        fig = plt.figure()
        ax1 = fig.add_axes([0.1, 0.7, 0.4, 0.2])
        ax2 = fig.add_axes([0.1, 0.4, 0.4, 0.2])
        ax3 = fig.add_axes([0.1, 0.1, 0.4, 0.2])
        ax4 = fig.add_axes([0.55, 0.25, 0.35, 0.5], projection='3d')

        # And we add vectors to each plot
        ax1.plot(t, x, color='red', lw=1, label='x(t)')
        ax1.set_xlabel('t')
        ax1.set_ylabel('x(t)')
        ax1.legend()
        ax1.axis((t_ini, t_fin, min(x), max(x)))

        ax2.plot(t, y, color='green', lw=1, label='y(t)')
        ax2.set_xlabel('t')
        ax2.set_ylabel('y(t)')
        ax2.legend()
        ax2.axis((t_ini, t_fin, min(y), max(y)))

        ax3.plot(t, z, color='blue', lw=1, label='z(t)')
        ax3.set_xlabel('t')
        ax3.set_ylabel('z(t)')
        ax3.legend()
        ax3.axis((t_ini, t_fin, min(z), max(z)))

        ax4.plot(x, y, z, color='black', lw=1, label='Evolution(t)')
        ax4.set_xlabel('x(t)')
        ax4.set_ylabel('y(t)')
        ax4.set_zlabel('z(t)')
        ax4.set_title('Evolution')

    return pd.Series(x), pd.Series(y), pd.Series(z)
