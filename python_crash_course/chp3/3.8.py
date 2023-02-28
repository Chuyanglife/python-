# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 20:20:20 2022

@author: User
"""

tour = ['Malaysia','China','Singapore','Taiwan','Australia']
print("Original order:")
print(tour)

print("\nAlphabetical:")
print(sorted(tour))

print("\nOriginal order:")
print(tour)

print("\nReverse Alphabetical:")
print(sorted(tour,reverse=True))

print("\nOriginal order:")
print(tour)

print("\nReversed:")
tour.reverse()
print(tour)

print("\nOrginal order:")
tour.reverse()
print(tour)

print("\nAlphabetical")
tour.sort()
print(tour)

print("\nReverse alphabetical")
tour.sort(reverse=True)
print(tour)








