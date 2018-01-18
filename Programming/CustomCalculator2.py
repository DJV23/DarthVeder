'''
CustomCalculator2.py
Ved Ballary
Last edit: 20th September 2017
V0.5
This program solves for the surface area of the cone
'''
from math import*
#making a custom calculator

'''
This is the input part of the program
'''
print("")

radius = input("Enter the length of the radius in metres: ")

print("")

height = input("Enter the height in metres: ")

A = pi * radius * (radius + sqrt(height ** 2  + radius ** 2))

print("")

'''
This is the output part of the program
'''

print("")

print("The surface area is  " + str(A))+"m"
