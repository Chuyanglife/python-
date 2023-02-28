# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 20:10:32 2022

@author: User
"""

guests = ['chuyang','junhan','wenbin','samuel','ricky']
print(f"\nWe got a bigger table!")
guests.insert(0,'lixiang')
guests.insert(3,'gavin')
guests.append('jason')
name = guests[0].title()
print(f"{name},please come to dinner.")
name = guests[1].title()
print(f"{name},please come to dinner.")
name = guests[2].title()
print(f"{name},please come to dinner.")
name = guests[3].title()
print(f"{name},please come to dinner.")
name = guests[4].title()
print(f"{name},please come to dinner.")
name = guests[5].title()
print(f"{name},please come to dinner.")
name = guests[6].title()
print(f"{name},please come to dinner.")
name = guests[7].title()
print(f"{name},please come to dinner.")

print(f"\nSorry,we can only invite two people to dinner.")
name = guests.pop()
print(f"Sorry,{name.title()} there's no room at the table.")
name = guests.pop()
print(f"Sorry,{name.title()} there's no room at the table.")
name = guests.pop()
print(f"Sorry,{name.title()} there's no room at the table.")
name = guests.pop()
print(f"Sorry,{name.title()} there's no room at the table.")
name = guests.pop()
print(f"Sorry,{name.title()} there's no room at the table.")
name = guests.pop()
print(f"Sorry,{name.title()} there's no room at the table.")
name = guests[0].title()
print(f"{name.title()},please come to dinner.")
name = guests[1].title()
print(f"{name.title()},please come to dinner.")
del guests[0]
del guests[0]
print(guests)




















