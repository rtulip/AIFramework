# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 18:29:19 2018

@author: Robbie Tulip
"""
import numpy as np
from random import random, seed, uniform
from copy import deepcopy
from Errors import *

#Credit to: https://gist.github.com/jovianlin/805189d4b19332f8b8a79bbd07e3f598
def sigmoid(x, derivative=False):
  return x*(1-x) if derivative else 1/(1+np.exp(-x))

class neuron:

    def __init__(self,shape):
        self.__weights = np.zeros(shape)
        
        a = np.sqrt(3 /shape)
        for i in range(len(self.__weights)):
            self.__weights[i] = uniform(-a,a)
        self.__shape = shape
        
    def __str__(self):
        return "Neuron Object of shape %i"%self.__shape
        
    def calculate(self,inputs):
        if len(inputs) != self.__shape:
            raise DifferentShapeError
        else:
            sm = np.dot(inputs,self.__weights)
            print (sigmoid(sm))
            return sigmoid(sm) 
    
    def get_weights(self):
        return self.__weights

    def set_weights(self,new_weights):
        if len(new_weights) != self.__shape:
            raise DifferentShapeError
        else:
            for i in range(self.__shape):
                if new_weights[i] < 0 or new_weights[i] > 1:
                    raise InvalidWeightError
                
            self.__weights = deepcopy(new_weights)
    
    def shape(self):
        return self.__shape
    
        
"""
seed(1001)

n = neuron(5)
print (n)
print (n.get_weights())

try:
    n.set_weights([random() for i in range(n.shape())])
except DifferentShapeError as e:
    print ("invalid set of weights")
except InvalidWeightError as e:
    print ("Invalid weights in inputs")

print (n.get_weights())
val = 0
try:
    val = n.calculate([random() for i in range(n.shape())])
except DifferentShapeError as e:
    print("Invalid Inputs: Different Shape")
finally:
    print (val)
 """   




        
            

