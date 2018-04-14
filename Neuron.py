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
    
def breed(neuron1,neuron2):
    
    if neuron1.shape() != neuron2.shape():
        raise DifferentShapeError
      
    new_neuron = neuron(neuron1.shape())
    new_weights = new_neuron.get_weights()
    weights1 = neuron1.get_weights()
    weights2 = neuron2.get_weights()
    for i in range(neuron1.shape()):
        random_num = random()
        if random_num < 1/3:
            #leave the weight the same
            new_weights[i] = weights1[i]
        elif random_num < 2/3:
            #use the other weight
            new_weights[i] = weights2[i]
        else:
            #use average
            new_weights[i] = np.average([weights1[i],weights2[i]])
    return new_neuron

"""
#seed(1001)

n1 = neuron(5)
print (n1.get_weights())

n2 = neuron(5)
print (n2.get_weights())

new = breed(n1,n2)

print (new.get_weights()) 
"""
 

  




        
            

