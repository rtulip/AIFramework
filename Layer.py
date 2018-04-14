# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 19:06:43 2018

@author: Robbie Tulip
"""
from random import random, seed
from Neuron import neuron, breed
from Errors import *


class layer:
    
    def __init__(self,shape,num_inputs):
        self.__shape = shape
        self.__neurons = []
        for i in range(self.shape()):
            self.__neurons.append(neuron(num_inputs))
        
    def __str__(self):
        return "A layer of shape %i. Nodes Require %i inputs each"%(self.__shape,self.__neurons[0].shape())
    
    def get_neurons(self):
        return self.__neurons
    
    def set_neurons(self,new_neurons):
        if len(new_neurons) != self.__shape:
            raise DifferentShapeError
        
        self.__neurons = new_neurons
    
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
    
def breed_layer(layer1,layer2):
    
    if layer1.shape() != layer2.shape():
        raise DifferentShapeError
    
    neurons1 = layer1.get_neurons()
    neurons2 = layer2.get_neurons()
    
    if neurons1[0].shape() != neurons2[0].shape():
        raise DifferentShapeError
    
    new_layer = layer(layer1.shape(),neurons1[0].shape())
    new_neurons = new_layer.get_neurons()
    for i in range(layer1.shape()):
        try:
            new_neurons[i] = breed(neurons1[i],neurons2[i])
        except Exception as e:
            handle(e)
            return False
        
    new_layer.set_neurons(new_neurons)
    return new_layer
        
        
                
        
"""      
seed(1001)
l  = layer(5,5)
print (l)

inputs = [random() for i in range(5)]       

print(l.collate(inputs)) 
"""   