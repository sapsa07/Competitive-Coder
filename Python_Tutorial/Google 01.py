"""
Given a number N, write a code to print all positive numbers less than N in which all adjacent digits differ by 1.

Ex : Input : 105
Output : 0,1,2,3,4,5,6,7,8,9,10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98,101

"""

n = int(input())

for i in range(0,n-1):
    if 