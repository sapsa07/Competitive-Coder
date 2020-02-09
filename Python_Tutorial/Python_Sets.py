# Python program to demonstrate sets 

Set = set([1,2]) 

print("Set: ") 
print(Set) 

# Adding element to the set 
Set.add(45)
Set.add(8)
Set.add(3)
Set.add(100)

print("\nSet after adding: ") 
print(Set) 

# Same as {"a", "b", "c"} 
Set = set(["a", "b", "c"]) 

print("Set: ") 
print(Set) 

# Adding element to the set 
Set.add("d") 

print("\nSet after adding: ") 
print(Set) 

# Python program to demonstrate differences 
# between normal and frozen set 

# Same as {"a", "b","c"} 
normal_set = set(["a", "b","c"]) 

print("Normal Set") 
print(normal_set) 

# A frozen set 
frozen_set = frozenset(["e", "f", "g"]) 

print("\nFrozen Set") 
print(frozen_set) 

# Uncommenting below line would cause error as 
# we are trying to add element to a frozen set 
# frozen_set.add("h")

# A Python program to demonstrate adding elements in a set 

# Creating a Set 
people = {"Jay", "Idrish", "Archi"} 

print("People:", end = " ") 
print(people) 

# This will add Daxit in the set 
people.add("Daxit") 

# Adding elements to the set using iterator 
for i in range(1, 6): 
    people.add(i) 

print("\nSet after adding element:", end = " ") 
print(people)

# Python Program to 
# demonstrate union of 
# two sets 

people = {"Jay", "Idrish", "Archil"} 
vampires = {"Karan", "Arjun"} 
dracula = {"Deepanshu", "Raju"} 

# Union using union() 
# function 
population = people.union(vampires) 

print("Union using union() function") 
print(population) 

# Union using "|" 
# operator 
population = people|dracula 

print("\nUnion using '|' operator") 
print(population)


# Python program to demonstrate intersection of two sets 

set1 = set() 
set2 = set() 

for i in range(5): 
    set1.add(i) 

for i in range(3,9): 
    set2.add(i) 

# Intersection using 
# intersection() function 
set3 = set1.intersection(set2)

print("Intersection using intersection() function") 
print(set3) 

# Intersection using "&" operator 
set3 = set1 & set2 

print("\nIntersection using '&' operator") 
print(set3)


# Python program to demonstrate difference of two sets 

set1 = set() 
set2 = set() 

for i in range(5): 
    set1.add(i) 

for i in range(3,9): 
    set2.add(i) 

# Difference of two sets using difference() function 
set3 = set1.difference(set2) 

print(" Difference of two sets using difference() function") 
print(set3) 

# Difference of two sets using '-' operator 
set3 = set1 - set2 

print("\nDifference of two sets using '-' operator") 
print(set3)


# Python program to demonstrate clearing of set 

set1 = {1,2,3,4,5,6} 

print("Initial set") 
print(set1) 

# This method will remove 
# all the elements of the set 
set1.clear() 

print("\nSet after using clear() function") 
print(set1)



# Python program to demonstrate working of 
# Set in Python 

# Creating two sets 
set1 = set() 
set2 = set() 

# Adding elements to set1 
for i in range(1, 6): 
    set1.add(i) 

# Adding elements to set2 
for i in range(3, 8): 
    set2.add(i) 

print("Set1 = ", set1) 
print("Set2 = ", set2) 
print("\n") 

# Union of set1 and set2 
set3 = set1 | set2# set1.union(set2) 
print("Union of Set1 & Set2: Set3 = ", set3) 

# Intersection of set1 and set2 
set4 = set1 & set2# set1.intersection(set2) 
print("Intersection of Set1 & Set2: Set4 = ", set4) 
print("\n") 

# Checking relation between set3 and set4 
if set3 > set4: # set3.issuperset(set4) 
    print("Set3 is superset of Set4") 
elif set3 < set4: # set3.issubset(set4) 
    print("Set3 is subset of Set4") 
else : # set3 == set4 
    print("Set3 is same as Set4") 

# displaying relation between set4 and set3 
if set4 < set3: # set4.issubset(set3) 
    print("Set4 is subset of Set3") 
    print("\n") 

# difference between set3 and set4 
set5 = set3 - set4 
print("Elements in Set3 and not in Set4: Set5 = ", set5) 
print("\n") 

# checkv if set4 and set5 are disjoint sets 
if set4.isdisjoint(set5): 
    print("Set4 and Set5 have nothing in common\n") 

# Removing all the values of set5 
set5.clear() 

print("After applying clear on sets Set5: ") 
print("Set5 = ", set5) 

