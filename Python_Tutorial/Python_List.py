# 1.Creating a List
List = [] 
print("Intial blank List: ") 
print(List) 

# Creating a List with the use of a String 
List = ['Saptarshi'] 
print("\nList with the use of String: ") 
print(List) 

# Creating a List with the use of multiple values 
List = ["Saptarshi", "Sabui", "Sapsa"] 
print("\nList containing multiple values: ") 
print(List[0]) 
print(List[2])

# Creating a Multi-Dimensional List (By Nesting a list inside a List) 
List = [['Geeks', 'For'] , ['Geeks']] 
print("\nMulti-Dimensional List: ") 
print(List) 

# 2. Creating a List with the use of Numbers (Having duplicate values) 
List = [1, 2, 4, 4, 3, 3, 3, 6, 5] 
print("\nList with the use of Numbers: ") 
print(List) 

# Creating a List with mixed type of values (Having numbers and strings) 
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks'] 
print("\nList with the use of Mixed Values: ") 
print(List)


#3. Python code to remove duplicate elements 
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

duplicate = [2,12,22,32,2,2]
print("\nPython Program to remove Duplicate Values :") 
print(Remove(duplicate))

#4. Adding Elements to List using append()
List = [] # Blank List
 
List.append(1) 
List.append(2) 
List.append(4) 
print("\nList after Addition of Three elements: ") 
print(List) 

# Adding elements to the List 
# using Iterator 
for i in range(1, 4): 
    List.append(i) 
print("\nList after Addition of elements from 1-3: ") 
print(List) 

# Adding Tuples to the List 
List.append((5, 6)) 
print("\nList after Addition of a Tuple: ") 
print(List) 

# Addition of List to a List 
List2 = ['For', 'Geeks'] 
List.append(List2) 
print("\nList after Addition of a List: ") 
print(List) 

# To demonstrate insert() of elements in a List 

# Creating a List 
List = [1,2] 
print("Initial List: ") 
print(List) 

# Addition of Element at specific Position using Insert Method, insert(position,value)
List.insert(3, 12) 
List.insert(0, 'Sap') 
print("\nList after performing Insert Operation: ") 
print(List) 


# Addition of multiple elements to the List at the end 
    
# Creating a List 
List = [1,2,3,4] 
print("Initial List: ") 
print(List) 

# (using Extend Method) 
List.extend([8, 'Geeks', 'Always']) 
print("\nList after performing Extend Operation: ") 
print(List) 



