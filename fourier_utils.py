# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:50:43 2015

@author: nicola
"""

import numpy as np

def eval_fourier_coeffs(order,fx,x):
    
    T = (x[-1]-x[0])
    
    omega = 2*np.pi/T
    
    ak = np.array([])
    bk = np.array([])
    
    a0 = 2./T * np.trapz(fx,x)
    ak = np.append(ak,[a0])
    
    for k in order[1:]:
        tmp = fx * np.cos(omega*k*x)
        tmp  = 2./T * np.trapz(tmp,x)
        ak = np.append(ak,[tmp])
        tmp = fx * np.sin(omega*k*x)
        tmp = 2./T * np.trapz(tmp,x)
        bk = np.append(bk,[tmp])

    return ak,bk
    
def eval_fourier_series(ak,bk,order,x):
    
    sf = ak[0]/2. * np.ones(x.shape)
    
    omega = 2*np.pi/(x[-1]-x[0])
    
    for a, b, k in zip(ak[1:],bk,order[1:]):
        sf += a * np.cos(omega*k*x) + b * np.sin(omega*k*x)
        
    return sf