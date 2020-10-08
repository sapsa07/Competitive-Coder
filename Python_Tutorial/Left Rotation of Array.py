T = int(input("Number of Test Cases :")) # Number of Test Cases

while T != 0:
    #Code Here
    
    n = int(input("Number of N :"))
    d = int(input("Number of D :"))
    
    lst= []
    
    for i in range(0,n):
        lst.append(int(input()))
        #end of for loop 
    print(lst[d:]+lst[:d])

    T-= 1 #end of while
