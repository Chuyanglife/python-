# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 19:57:49 2022

@author: User
"""

guests = ['chuyang','yingcong','junhan']
name = guests[0].title()
print(f"{name},please come to dinner.")
name = guests[1].title()
print(f"{name},please come to dinner.")
name = guests[2].title()
print(f"{name},please come to dinner.")

name = guests[1].title()
print(f"\nSorry,{name} can't make it to dinner.")

del(guests[1])
guests.insert(1,'wenbin')

name = guests[0].title()
print(f"{name},please come to dinner.")
name = guests[1].title()
print(f"{name},please come to dinner.")
name = guests[2].title()
print(f"{name},please come to dinner.")