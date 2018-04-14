# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 19:06:43 2018

@author: Robbie Tulip
"""
from random import random, seed
from Node import neuron
from Errors import *


class layer:
    
    def __init__(self,shape,num_inputs):
        self.__shape = shape
        self.__neurons = []
        for i in range(self.__shape):
            self.__neurons.append(neuron(num_inputs))
        
    def __str__(self):
        return "A layer of shape %i. Nodes Require %i inputs each"%(self.__shape,self.__neurons[0].shape())
    
    def get_nodes(self):
        return self.__neurons
    
    def collate(self,inputs):
        output = []
        try:
            for n in self.__neurons:
                print (n,n.get_weights())
                output.append(n.calculate(inputs))
        except Exception as e:
            handle(e)
            return False
        else:
            return output
    
    def shape(self):
        return self.__shape
        
                
        
"""      
seed(1001)
l  = layer(5,5)
print (l)

inputs = [random() for i in range(5)]       

print(l.collate(inputs)) 
"""   