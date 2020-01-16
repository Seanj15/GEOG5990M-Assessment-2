# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:37:16 2020

@author: Sean

This file contains an agent class. The agents (or drunks) have a location 
(x and y coordinates) in a 2D grid represented by a raster environment.
Each agent will move around in the 2D grid to find their assigned home.
"""

import random 

class Drunk():
    def __init__(self, environment, drunks, house_number):
        """ Set the parameters for the drunks class in the model"""
        self.environment = environment
        self.drunks = drunks
        self.house_number = house_number
        self.x = 138 # random x coordinate in the pub
        self.y = 145 # random y coordinate in the pub
        self.home = False 
        
    def move(self): 
        """ 
        Make the drunks move randomly around the environment.
        You can alter the speed at which the drunks move by changing 
        the number next to 'drunk_speed'.
        """
        drunk_speed = 5 # Feel free to edit the speed of the drunks by changing this number 
        
        if random.random() < 0.5:
            self.x = (self.x + drunk_speed) # Move the agent right 
        else:
            self.x = (self.x - drunk_speed) # Move the agent left
    
        if random.random() < 0.5:
            self.y = (self.y + drunk_speed) # Move the agent up
        else:
            self.y = (self.y - drunk_speed) # Move the agent down
    
        """
        Boundary edge:
         - Stops the drunks wandering off the edge of the environment.
         - Prevents them from reappearing on the opposite side of the screen.
         """
        if self.x < 0: 
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > len(self.environment) -1:
            self.x = len(self.environment) -1
        if self.y > len(self.environment) -1:
            self.y = len(self.environment) -1
        
        """
        To develop the model further, it would be beneficial to stop 
        the agents retracing their steps
        """
    