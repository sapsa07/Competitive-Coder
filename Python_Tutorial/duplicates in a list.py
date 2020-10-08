# Step 1
MyList = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']

my_dict = {i:MyList.count(i) for i in MyList}
print(my_dict)

# Key pairs whose value is greater than 1 i.e. only duplicate elements from list.
my_dict = {i:MyList.count(i) for i in MyList if MyList.count(i) > 1}
print(my_dict)

# Step 2 using Counter Module
from collections import Counter 

listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
 
# Create a dictionary of elements & their frequency count
dictOfElems = dict(Counter(listOfElems))
 
# Remove elements from dictionary whose value is 1, i.e. non duplicate items
dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
 
for key, value in dictOfElems.items():
        print('Element = ' , key , ' :: Repeated Count = ', value)
# Get indices of each duplicate element in a list along with frequency count

def getDuplicatesWithInfo(listOfElems):
    ''' Get duplicate element in a list along with thier indices in list
     and frequency count'''
    dictOfElems = dict()
    index = 0
    # Iterate over each element in list and keep track of index
    for elem in listOfElems:
        # If element exists in dict then keep its index in list & increment its frequency
        if elem in dictOfElems:
            dictOfElems[elem][0] += 1
            dictOfElems[elem][1].append(index)
        else:
            # Add a new entry in dictionary 
            dictOfElems[elem] = [1, [index]]
        index += 1    
 
    dictOfElems = { key:value for key, value in dictOfElems.items() if value[0] > 1}
    # dictOfElems = { key:value for key, value in dictOfElems.items() if value[0] > 1}
    return dictOfElems


# List of strings
listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
 
dictOfElems = getDuplicatesWithInfo(listOfElems)
 
for key, value in dictOfElems.items():
        print('Element = ', key , ' :: Repeated Count = ', value[0] , ' :: Index Positions =  ', value[1])
        

# https://thispointer.com/python-find-duplicates-in-a-list-with-frequency-count-index-positions/