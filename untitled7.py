# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 20:34:06 2022

@author: kelvi
"""

class Pet:
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner
    
   
    
class Dog(Pet):
    def __init__(self,name,owner,gender):
        super().__init__(self,name,owner)
        self.gender = gender

Pet1 = Pet('Huggy Wuggy','Sean')
    
print(Pet1.name)
print(Pet1.owner)



   
    
    
    
    
    
    
    
    
    
    