# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:04:31 2015

@author: nicola
"""

import numpy as np

def define_continuous(x,L):
    fx = x*(L-x);    
    return fx
    
def define_discontinuous(x,L):
    fx = np.zeros(x.shape)
    fx[np.nonzero((x>2) & (x<3))] = 1
    return fx