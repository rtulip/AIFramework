# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 00:34:46 2018

@author: Robbie Tulip
"""

from random import random,seed
from Errors import *
from Layer import layer

class network():
    
    def __init__(self,input_shape,num_hidden_layers,hidden_layer_shape,output_layer_shape):
        self.__hidden_layers = [layer(hidden_layer_shape,input_shape)]
        for i in range(num_hidden_layers-1):
            self.__hidden_layers.append(layer(hidden_layer_shape,hidden_layer_shape))
        self.__output_layer = layer(output_layer_shape,hidden_layer_shape)
        self.__num_layers = num_hidden_layers + 1
        self.__input_shape = input_shape
        
    def __str__(self):
        return ("This is a network Object with %i layers. An input of size %i is required. This network object produces an output of size %i\n"%(self.__num_layers,self.__input_shape,self.__output_layer.shape()))
    
    def print_layers(self): 
        for l in self.__hidden_layers:
            print (l)
        print(self.__output_layer)

    def iterate(self,inputs):
        try:
            for l in self.__hidden_layers:
                print (l)
                print ("inupts: %s"%str(inputs))
                inputs = l.collate(inputs)
            inputs = self.__output_layer.collate(inputs)
        except Exception as e:
            handle(e)
            return False
        else:
            return inputs
"""
seed(101)

net = network(105,2,32,8)
print(net)
inputs = [random() for i in range(104)]
inputs.append(1)
print (net.iterate(inputs))
"""