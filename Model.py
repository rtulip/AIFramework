# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 10:21:28 2018

@author: Robbie Tulip
"""
from random import sample
import numpy as np
from Network import network

class neuroEvolution():
    
    def __init__(self, networks):
        
        self.__networks = sorted(networks,key = lambda x:x[1],reverse = True)
        self.__size = len(self.__networks)
        self.__mean = (int(len(self.__networks)/2))
    
    def __str__(self):
        return str(self.__networks)
        
    def cull(self):
        
        self.__networks = self.__networks[0:self.__mean]
        self.__size = len(self.__networks)  
        
    def breed(self):
        
        for i in range(self.__size):
            pair = sample(self.__networks,2)
            
            
            
        


networks = []   
for i in range(10):
    networks.append((network(5,2,3,2),i))

model = neuroEvolution(networks)
model.cull()
model.breed()


        