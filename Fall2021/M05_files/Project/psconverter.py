#!usr/bin/env python3

#Name: (Peter Sanford)
#Class: (INFO 1200)
#Section: (001)
#Professor: (Crandall)
#Date:  10/9/21
#Project #: MO5_P2_converter
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

'''
Fuction that converts feet to meters
'''
def to_meters(feet): # Sets the function name to to_meters with one parameter
    meters = feet * 0.3048 # Sets new variable meters to feet * .3048
    return meters # returns the meters value to the to_meters fuction

'''
Function that converts meters to feet
'''
def to_feet(meters): # Sets the function name to to_feet with one parameter
    feet = meters / 0.3048 # Sets new variable feet to meters / .3048
    return feet # returns the feet value to the to_feet function

