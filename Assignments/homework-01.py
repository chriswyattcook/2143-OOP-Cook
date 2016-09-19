"""
Name: Chris Cook
Email: c.w.cook@live.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 19 Sep @ 1:00 p.m.
"""

#A
a=[1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1 3

a[4] = a[2] + a[-2]
print(a)
# Prints: [1,5,4,2,6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: true

a[1] = [a[1], a[0]]
print(a)
# Prints: [1,[5,1],4,2,6]

#B
"""Removes all instances of el from lst. 
Given: x = [3, 1, 2, 1, 5, 1, 1, 7]
Usage: remove_all(1, x)
Would result in: [3, 2, 5, 7]
"""
def remove_all(el, lst):
   while (el in lst):
       lst.remove(el)

#C
""" Adds y to the end of lst the number of times x occurs in lst. 
Given: lst = [1, 2, 4, 2, 1]
Usage: add_this_many(1, 5, lst)
Results in: [1, 2, 4, 2, 1, 5, 5]
"""
def add_this_many(x, y, lst):
    for i in range(len(a)):
        if (lst[i] == x):
            lst.append(y)
        i += 1

#D
a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print(a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: [1, 2, 3]

print(a[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1, 4, 2]

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]

#E
#Source for code:
#https://pythonadventures.wordpress.com/2011/06/29/reverse-a-string-or-list-in-place/
""" Reverses lst in place. 
Given: x = [3, 2, 4, 5, 1] 
Usage: reverse(x)
Results: [1, 5, 4, 2, 3]
"""
def reverse(lst):
    for i in range(len(lst)//2):
        lst[i], lst[ len(lst) -1 - i] = lst[ len(lst) -1 - i], lst[i]

x = [3, 2, 4, 5, 1] 
reverse(x)
print(x)

#F
""" Return a new list, with the same elements of lst, rotated to the right k.
Given: x = [1, 2, 3, 4, 5]
Usage: rotate(x, 3)
Results: [3, 4, 5, 1, 2]
"""
def rotate(lst, k):
    for i in range(0,k):
        p = lst[0] 
        lst.pop(0)
        lst.append(p)
        i+=1

#H
print('colin kaepernick' in superbowls)
#Prints: false

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: false

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {('eli manning', 'giants'): 2, 'tom brady': 3, 'joe montana': 4, 'peyton manning': 1, 'joe flacco': 1}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {('eli manning', 'giants'): 2, 3: 'cat', 'joe montana': 4, 'peyton manning': 1, 'joe flacco': 1, 'tom brady': 3}

superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {('eli manning', 'giants'): 5, 3: 'cat', 'joe montana': 4, 'peyton manning': 1, 'joe flacco': 1, 'tom brady': 3}

superbowls[['steelers', '49ers']] = 11
print(superbowls)
#Prints: ??

