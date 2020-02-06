# Python Program to detect if two strings are anagrams using Sorted()
"""
def check(s1, s2): 
    
    # the sorted strings are checked 
    if(sorted(s1)== sorted(s2)): 
        print("The strings are anagrams.") 
    else: 
        print("The strings aren't anagrams.")        
        

s1 = input("Enter String 1 :")
s2 = input("Enter String 2 :")
check(s1, s2) 
 
"""

# Python Program to detect if two strings are anagrams

def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)

# main

s1 = input("Enter String 1 :")
s2 = input("Enter String 2 :")

print(is_anagram(s1,s2))
