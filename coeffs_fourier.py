# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:11:37 2015

@author: nicola
"""

import numpy as np
import matplotlib.pyplot as plt

import fourier_utils as fu

def main():
    
    order = np.arange(0,8)
    #x = np.linspace(-np.pi,np.pi,100)
    x = np.linspace(-5,5,100)
    fx = x**2;
    
    ak, bk = fu.eval_fourier_coeffs(order,fx,x)
    
    sf = fu.eval_fourier_series(ak,bk,order,x)
            
    plt.plot(x,fx)
    plt.plot(x,sf,'-g')
    plt.show()

    print 'stocazzo'
    
    return

if __name__ == "__main__":
    main()
    