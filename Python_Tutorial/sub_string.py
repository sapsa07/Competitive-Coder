# Python : Check if a String contains a sub string & find it’s index | Case insensitive

Python : Check if a String contains a sub string & find it’s index | case insensitiveVarun April 7, 2019 Python : Check if a String contains a sub string & find it’s index | case insensitive2019-04-07T07:21:49+05:30Python, strings No Comment
In this article we will discuss different ways to check if a sub-string exists in another string and if yes then find it’s index. Will also explore ways to check the existence of sub-string in case in-sensitive manner by ignoring case.


Check if a String contains another string or character using “in” and “not in” operator
in Operator
Python provides an in operator that can be used to check if a given character or string exists in another string. For example,

mainStr = "This is a sample String with sample message."
# Use in operator to check if sub string exists in another string
if "sample" in mainStr:
print ('Sub-string Found')
else:
print('Sub-string not found')
1
2
3
4
5
6
7
mainStr = "This is a sample String with sample message."
 
# Use in operator to check if sub string exists in another string
if "sample" in mainStr:
   print ('Sub-string Found')
else:
   print('Sub-string not found')
Output:

Sub-string Found
1
Sub-string Found
As our main string contains the sub-string ‘sample’ therefore in operator returned True.

not in Operator
Similarly we can also use “not in” operator to check the opposite scenario i.e. check if a string or character doesn’t exists in an another string. For example,

mainStr = "This is a sample String with sample message."
if "Hello" not in mainStr:
print ("Sub-string Doesn't exists in main String")
1
2
3
4
mainStr = "This is a sample String with sample message."
 
if "Hello" not in mainStr:
   print ("Sub-string Doesn't exists in main String")
Output:

Sub-string Doesn't exists in main String
1
Sub-string Doesn't exists in main String
As our main string doesn’t contains the sub-string ‘Hello’ therefore ‘not in’ operator returned True.

Ignore case : Check if a String contains another string in case-insensitive manner
To check if a given string or a character exists in an another string or not in case insensitive manner i.e. by ignoring case, we need to first convert both the strings to lower case then use “ïn” or “not ïn” operator to check the membership of sub string.For example,

mainStr = "This is a sample String with sample message."
# use in operator to check if sub string exists by ignoring case of strings
# Convert both the strings to lower case then check for membership using in operator
if "SAMple".lower() in mainStr.lower():
print('Sub-string Found')
else:
print('Sub-string not found')
1
2
3
4
5
6
7
8
mainStr = "This is a sample String with sample message."
 
# use in operator to check if sub string exists by ignoring case of strings
# Convert both the strings to lower case then check for membership using in operator
if "SAMple".lower() in mainStr.lower():
   print('Sub-string Found')
else:
   print('Sub-string not found')
output:

Sub-string Found
1
Sub-string Found

 
Check if a String contains any string from a List
Suppose we have a list of strings and a big main string i.e.

mainStr = "This is a sample String with sample message."
listOfstrs = ['Hello', 'here', 'with', 'here', 'who']
1
2
3
mainStr = "This is a sample String with sample message."
 
listOfstrs = ['Hello', 'here', 'with', 'here', 'who']
Now we need to check if any of the string from the list exists in the main string or not. For this we have two techniques,
Technique 1 : Using for loop

Let’s create a function that will iterate through all the lists in given list and check for their membership in the main list i.e.

'''
Check if string mainStr contains any string from the list of strsing passed i.e. listOfStr
If any string is found then return a tuple of True & string that is found
else return a tuple of False & empty string.
'''
def checkIfAny(mainStr, listOfStr):
for subStr in listOfStr:
if subStr in mainStr:
return (True, subStr)
return (False, "")
1
2
3
4
5
6
7
8
9
10
'''
Check if string mainStr contains any string from the list of strsing passed i.e. listOfStr
If any string is found then return a tuple of True & string that is found
else return a tuple of False & empty string.
'''
def checkIfAny(mainStr, listOfStr):
   for subStr in listOfStr:
       if subStr in mainStr:
           return (True, subStr)
   return (False, "")
Now let’s use this function to check if any string from the list exists in the main string or not,

# Check if mainStr string contains any string from the list
result = checkIfAny(mainStr, listOfstrs)
if result[0]:
print('Sub-string Found in main String : ', result[1])
1
2
3
4
# Check if mainStr string contains any string from the list
result = checkIfAny(mainStr, listOfstrs)
if result[0]:
   print('Sub-string Found in main String : ', result[1])
Output:

Sub-string Found in main String :  with
1
Sub-string Found in main String :  with
Well it worked, but creating a separate function with so many lines is not pythonic. What if we could do all this in a single line ?
Let’s see how to do that

Technique 1 : Using any() and List comprehension

In Python any(iterable) function accepts an iterable as an argument and returns if any element in the iterable is True. Let’s use any() to check if a given String contains any string from a List i.e.

# Check if any string from the list exists in given string
result = any(([True if subStr in mainStr else False for subStr in listOfstrs]))
if result:
print('A string from list Found in main String ')
1
2
3
4
5
# Check if any string from the list exists in given string
result = any(([True if subStr in mainStr else False for subStr in listOfstrs]))
 
if result:
   print('A string from list Found in main String ')
Output:

A string from list Found in main String
1
A string from list Found in main String
We iterated over the list of strings using list of comprehension and created a new bool list and then passed it to any().

Check if a String contains all string from a List
In Python all(iterable) function accepts an iterable as an argument and returns if all element in the iterable are True. We can use List comprehension and all() to check if all elements from a list exists in the given string i.e.

mainStr = "This is a sample String with sample message."
listOfstrs = ['sample', 'String', 'with']
# Check if all strings from the list exists in given string
result = all(([True if subStr in mainStr else False for subStr in listOfstrs]))
if result:
print('All strings from list Found in main String ')
1
2
3
4
5
6
7
8
mainStr = "This is a sample String with sample message."
listOfstrs = ['sample', 'String', 'with']
 
# Check if all strings from the list exists in given string
result = all(([True if subStr in mainStr else False for subStr in listOfstrs]))
 
if result:
   print('All strings from list Found in main String ')
Output:

All strings from list Found in main String
1
All strings from list Found in main String
Python Regex : Check if a String contains another string using regex
We can also use python’s regex module to check if a given string exists in another string in both case sensitive and insensitive manner i.e.

Case sensitive Approach:

Create a pattern to match string i.e.

# Create a pattern to match string 'sample'
patternObj = re.compile("sample")
1
2
# Create a pattern to match string 'sample'
patternObj = re.compile("sample")
Now search for the pattern inside the string for match using pattern.search(). If match is found then it will return a Match Object else None i.e.

mainStr = "This is a sample String with sample message."
# search for the pattern in the string and return the match object
matchObj = patternObj.search(mainStr)
# check if match object is not Null
if matchObj:
print('Sub-string Found')
else:
print('Sub-string Not Found')
1
2
3
4
5
6
7
8
9
10
mainStr = "This is a sample String with sample message."
 
# search for the pattern in the string and return the match object
matchObj = patternObj.search(mainStr)
 
# check if match object is not Null
if matchObj:
   print('Sub-string Found')
else:
   print('Sub-string Not Found')
Output:

Sub-string Found
1
Sub-string Found
Ignore case : check if a string exists in another string in case insensitive approach
Use re.search() to find the existence of a sub-string in the main string by ignoring case i.e.

# search for the sub-string in string by ignoring case
matchObj =  re.search('SAMple', mainStr, flags=re.IGNORECASE)
if matchObj:
print('Sub-string Found')
else:
print('Sub-string Not Found')
1
2
3
4
5
6
7
# search for the sub-string in string by ignoring case
matchObj =  re.search('SAMple', mainStr, flags=re.IGNORECASE)
 
if matchObj:
   print('Sub-string Found')
else:
   print('Sub-string Not Found')
Output:

Sub-string Found
1
Sub-string Found
Complete example is as follows,

import re
'''
Check if string mainStr contains any string from the list of strsing passed i.e. listOfStr
If any string is found then return a tuple of True & string that is found
else return a tuple of False & empty string.
'''
def checkIfAny(mainStr, listOfStr):
for subStr in listOfStr:
if subStr in mainStr:
return (True, subStr)
return (False, "")
def main():
print('**** Check if a String contains another string in case sensitive manner ****')
mainStr = "This is a sample String with sample message."
# Use in operator to check if sub string exists in another string
if "sample" in mainStr:
print ('Sub-string Found')
else:
print('Sub-string not found')
if "Hello" not in mainStr:
print ("Sub-string Doesn't exists in main String")
print('**** Ignore case : Check if a String contains another string in case-insensitive manner ****')
# use in operator to check if sub string exists by ignoring case of strings
# Convert both the strings to lower case then check for membership using in operator
if "SAMple".lower() in mainStr.lower():
print('Sub-string Found')
else:
print('Sub-string not found')
print('**** Check if a String contains any string from a list ****')
listOfstrs = ['Hello', 'here', 'with', 'here', 'who']
# Check if mainStr string contains any string from the list
result = checkIfAny(mainStr, listOfstrs)
if result[0]:
print('Sub-string Found in main String : ', result[1])
print('Using List comprehension and any() ')
# Check if any string from the list exists in given string
result = any(([True if subStr in mainStr else False for subStr in listOfstrs]))
if result:
print('A string from list Found in main String ')
print('**** Check if a String contains any string from a list ****')
listOfstrs = ['sample', 'String', 'with']
# Check if all strings from the list exists in given string
result = all(([True if subStr in mainStr else False for subStr in listOfstrs]))
if result:
print('All strings from list Found in main String ')
print('**** Regex : Check if a String contains another string using Python Regex ****')
# Create a pattern to match string 'sample'
patternObj = re.compile("sample")
# search for the pattern in the string and return the match object
matchObj = patternObj.search(mainStr)
# check if match object is not Null
if matchObj:
print('Sub-string Found')
else:
print('Sub-string Not Found')
print('**** Python Regex : Check if a String contains another string in Case in sensitive manner | ignore case ****')
# search for the sub-string in string by ignoring case
matchObj =  re.search('SAMple', mainStr, flags=re.IGNORECASE)
if matchObj:
print('Sub-string Found')
else:
print('Sub-string Not Found')
if __name__ == '__main__':
main()

import re
 
'''
Check if string mainStr contains any string from the list of strsing passed i.e. listOfStr
If any string is found then return a tuple of True & string that is found
else return a tuple of False & empty string.
'''
def checkIfAny(mainStr, listOfStr):
   for subStr in listOfStr:
       if subStr in mainStr:
           return (True, subStr)
   return (False, "")
 
 
def main():
 
 
    print('**** Check if a String contains another string in case sensitive manner ****')
 
    mainStr = "This is a sample String with sample message."
 
    # Use in operator to check if sub string exists in another string
    if "sample" in mainStr:
       print ('Sub-string Found')
    else:
       print('Sub-string not found')
 
    if "Hello" not in mainStr:
       print ("Sub-string Doesn't exists in main String")
 
    print('**** Ignore case : Check if a String contains another string in case-insensitive manner ****')
 
    # use in operator to check if sub string exists by ignoring case of strings
    # Convert both the strings to lower case then check for membership using in operator
    if "SAMple".lower() in mainStr.lower():
       print('Sub-string Found')
    else:
       print('Sub-string not found')
 
    print('**** Check if a String contains any string from a list ****')
 
    listOfstrs = ['Hello', 'here', 'with', 'here', 'who']
 
    # Check if mainStr string contains any string from the list
    result = checkIfAny(mainStr, listOfstrs)
    if result[0]:
       print('Sub-string Found in main String : ', result[1])
 
    print('Using List comprehension and any() ')
 
    # Check if any string from the list exists in given string
    result = any(([True if subStr in mainStr else False for subStr in listOfstrs]))
 
    if result:
       print('A string from list Found in main String ')
 
    print('**** Check if a String contains any string from a list ****')
 
    listOfstrs = ['sample', 'String', 'with']
 
    # Check if all strings from the list exists in given string
    result = all(([True if subStr in mainStr else False for subStr in listOfstrs]))
 
    if result:
       print('All strings from list Found in main String ')
 
 
    print('**** Regex : Check if a String contains another string using Python Regex ****')
 
    # Create a pattern to match string 'sample'
    patternObj = re.compile("sample")
 
    # search for the pattern in the string and return the match object
    matchObj = patternObj.search(mainStr)
 
    # check if match object is not Null
    if matchObj:
       print('Sub-string Found')
    else:
       print('Sub-string Not Found')
 
    print('**** Python Regex : Check if a String contains another string in Case in sensitive manner | ignore case ****')
 
    # search for the sub-string in string by ignoring case
    matchObj =  re.search('SAMple', mainStr, flags=re.IGNORECASE)
 
    if matchObj:
       print('Sub-string Found')
    else:
       print('Sub-string Not Found')
 
if __name__ == '__main__':
  main()
Output:

Vim
**** Check if a String contains another string in case sensitive manner ****
Sub-string Found
Sub-string Doesn't exists in main String
**** Ignore case : Check if a String contains another string in case-insensitive manner ****
Sub-string Found
**** Check if a String contains any string from a list ****
Sub-string Found in main String :  with
Using List comprehension and any() 
A string from list Found in main String 
**** Check if a String contains any string from a list ****
All strings from list Found in main String 
**** Regex : Check if a String contains another string using Python Regex ****
Sub-string Found
**** Python Regex : Check if a String contains another string in Case in sensitive manner | ignore case ****
Sub-string Found

**** Check if a String contains another string in case sensitive manner ****
Sub-string Found
Sub-string Doesn't exists in main String
**** Ignore case : Check if a String contains another string in case-insensitive manner ****
Sub-string Found
**** Check if a String contains any string from a list ****
Sub-string Found in main String :  with
Using List comprehension and any() 
A string from list Found in main String 
**** Check if a String contains any string from a list ****
All strings from list Found in main String 
**** Regex : Check if a String contains another string using Python Regex ****
Sub-string Found
**** Python Regex : Check if a String contains another string in Case in sensitive manner | ignore case ****
Sub-string Found