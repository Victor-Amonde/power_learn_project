#!/usr/bin/env python3

"""
"""

my_list = []
list_1 = [10, 20, 30, 40]
for i in list_1:
    my_list.append(i)
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.pop()
my_list.sort()
indx = my_list.index(30)
print("index of the value 30 is: ", indx)
