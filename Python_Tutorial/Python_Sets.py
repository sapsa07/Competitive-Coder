"""
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

"""


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
