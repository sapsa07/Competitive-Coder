"""
A rotation on a string is defined as removing first element
and concatenating it at the end

Given N
and an array of N strings
Output the minimum no. of rotations on the strings so as to make all the strings
equal.
If this is not possible return -1

example
4
11234
34112
41123
11234
output
3

finally all the strings would be 11234
first and last string input needs no rotations
second needs 2 rotations
third 1 rotation

"""

def rotate(arr):
    if not arr: return -1
    n = len(arr[0])
    cnt = {(arr[0][i:] + arr[0][:i]) : i for i in range(n)}
    for s in arr[1:]:
        if len(s) != n: return -1
        for i in range(n):
            cur = s[i:] + s[:i]
            if cur not in cnt: return -1
            cnt[cur] += i
    return cnt[min(cnt, key = lambda x: cnt[x])]

T = int(input("Number of Test Cases")) # Number of Test Cases

while T != 0:
    #Code Here
    
    n = int(input("Number of Elements"))
    
    lst= []
    
    for i in range(0,n):
        ele = input()
        lst.append(ele)
        
        #end of for loop 
    print(rotate(lst))
    
    T-= 1 #end of while