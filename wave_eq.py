# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:11:37 2015

@author: nicola
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

import fourier_utils as fu

def evaluate_solution(omega,c,time,x,bk,order):
    sol = np.zeros([0,len(x)])
        
    for t in time:
        u = np.zeros(x.shape)
        for b, k in zip(bk,order[1:]):
            u += b*np.cos(c*omega*k*t)*np.sin(omega*k*x)
        sol = np.vstack([sol,u])

    return sol
    
def plot_solution(time,x,sol):

    T,X = np.meshgrid(x,time)
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface( T, X, sol, rstride=1, cstride=1, cmap=cm.jet,
        linewidth=0, antialiased=False)
        
    ax.set_xlabel('x')
    ax.set_ylabel('t')
        
    plt.show()

    return

def main():
    
    order = np.arange(0,8)    
    c = 1
    L = 5
    omega = np.pi/L
    
    x = np.linspace(0,L,100)
    
    fx = define_continuous_ic(x,L)

    ak, bk = fu.eval_fourier_coeffs(order,
                                    np.hstack([-1*fx[::-1],fx]),
                                    np.hstack([-1*x[::-1],x]))
    
    time = np.linspace(0,5,40)
    
    sol = evaluate_solution(omega,c,time,x,bk,order)
    
    plot_solution(time,x,sol)

    return

if __name__ == "__main__":
    main()
    
