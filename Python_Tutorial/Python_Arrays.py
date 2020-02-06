# Python program to take input from users
arr = []

n = int(input("Enter No. Element :"))

for i in range(0,n):
    ele = int(input())
    arr.append(ele)
    
print(arr)

# Python program to take input from users with exception handling

lst = []

n = int(input("Enter No. Element :"))

try:
    while True:
        lst.append(int(input()))
        
except:
    print(lst)

# Using map()

n = int(input("Enter No. Element :"))

# Below lines read inputs from user using map()
for i in range(0,n):
    a = list(map(int,input("\nEnter the numbers :").strip().split()))

print("\nList - ",a)


# list of list as input ie 2D Matrix

lst1 = []

n = int(input("Enter No. Element :"))

for i in range(0,n):
    ele = [int(input()),int(input())]
    lst1.append(ele)

print(lst1)


# Matrix input from user in Python

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of rows:"))

matrix = []

print("Enter the entries rowise :")

for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

print("\nMatrix :")

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()