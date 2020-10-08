"""
Given a list of tuples,write a Python program to check if an element of the list has duplicates.
If duplicate exist, print the number of occurrence of each duplicate tuple,
otherwise print “No Duplicates”.
"""

def dup(lst):
    flag = False
    
    col_list = []
    col_cnt = 0
    
    for t in lst:
        flag = True
        continue


lst = [('a', 'e'), ('b', 'x'), ('b', 'x'), ('a', 'e'), ('b', 'x')]

dup(lst)