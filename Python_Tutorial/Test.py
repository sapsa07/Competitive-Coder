

T = int(input("Number of Test Cases")) # Number of Test Cases

while T != 0:
    #Code Here
    
    n = int(input("Number of Elements"))
    
    lst= []
    
    for i in range(0,n):
        ele = input()
        lst.append(ele)
        
    print(lst)
    print(lst[:2])
        
        #end of for loop 
    
    T-= 1 #end of while
