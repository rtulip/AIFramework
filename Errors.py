# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 19:17:32 2018

@author: Robbie Tulip
"""

class DifferentShapeError(Exception):
    pass

class InvalidWeightError(Exception):
    pass


def handle(e):
    
    if type(e) == DifferentShapeError:
        print ("Invalid Shape Argument")
    elif type(e) == InvalidWeightError:
        print ("Input containted an invalid weight. 0 <= w <= 1")
    else:
        print ("Unknown Error Occurred")
        