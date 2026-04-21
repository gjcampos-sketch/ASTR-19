# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:02:33 2026

@author: theja
"""

class Giraffe:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        #all in meters
        self.arm_length = float(arm_length)   
        self.leg_length = float(leg_length)    
        self.num_eyes = int(num_eyes)          
        self.has_tail = bool(has_tail)         
        self.is_furry = bool(is_furry)         
        
    def describe_giraffe(self):
        print("Physical characteristics of this giraffe:")
        print(f"Length of arms: {self.arm_length}")
        print(f"Length of legs: {self.leg_length}")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has a tail?    {self.has_tail}")
        print(f"Is it furry?   {self.is_furry}")

def main():
    my_giraffe = Giraffe(1.5, 2.0, 2, True, True)
    my_giraffe.describe_giraffe()

if __name__ == "__main__":
    main()