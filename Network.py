# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 00:34:46 2018

@author: Robbie Tulip
"""

from random import random,seed
from Errors import *
from Layer import layer, breed_layer

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
    
    def shape(self):
        return self.__num_layers
    
    def get_layers(self):
        return self.__hidden_layers, self.__output_layer
    
    def set_layers(self,new_hidden_layers,new_output_layer):
        if len(new_hidden_layers) != len(self.__hidden_layers):
            raise DifferentShapeError
        
        for i in range(len(new_hidden_layers)):
            if self.__hidden_layers[i].shape() != new_hidden_layers[i].shape():
                raise DifferentShapeError
            
            if self.__hidden_layers[i].get_neurons()[0].shape() != new_hidden_layers[i].get_neurons()[0].shape():
                raise DifferentShapeError
            
            self.__hidden_layers[i] = new_hidden_layers[i]
       
        if self.__output_layer.shape() != new_output_layer.shape():
                raise DifferentShapeError
            
        if self.__output_layer.get_neurons()[0].shape() != new_output_layer.get_neurons()[0].shape():
            raise DifferentShapeError
            
        self.__output_layer = new_output_layer
        
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
        
def breed_network(network1,network2):
    
    if network1.shape() != network2.shape():
        raise DifferentShapeError
    
    hidden1, output1 = network1.get_layers()
    hidden2, output2 = network2.get_layers()
    
    new_network = network(hidden1[0].get_neurons()[0].shape(),len(hidden1),hidden1[0].shape(),output1.shape())
    new_hidden_layers,new_output_layer = new_network.get_layers()
    
    for i in range(len(hidden1)):
        try:
            new_hidden_layers[i] = breed_layer(hidden1[i],hidden2[i])
        except Exception as e:
            handle(e)
    new_output_layer = breed_layer(output1,output2)
    
    new_network.set_layers(new_hidden_layers,new_output_layer)
    
    return new_network
            
"""
seed(101)

n1 = network(105,2,32,8)
n2 = network(105,2,32,8)

breed_network(n1,n2)
"""