# 						**Python Tutorial**

## **Python Arrays**

Python has 3 main sequence classes:

- List : [1,2,3]
- Tuple : (1,2,3)
- String : '123'

All support indexing (**e.g.** t[0] = 1) 

## Python List

<u>**Python List :**</u> **Lists** are just like the **arrays, declared in other languages**. <u>Lists need not be homogeneous always which makes it a most powerful tool in Python.</u> A single list may contain Data Types like Integers, Strings, as well as Objects. 

- List in Python are ordered and have a definite count. 

- <u>Lists are mutable, and hence, they can be altered even after their creation.</u>

- The elements in a list are indexed according to a definite sequence and the indexing of a list is done with 0 being the first index.

- Each element in the list has its definite place in the list, which allows duplicating of elements in the list, with each element having its own distinct place and credibility.

- Lists in Python can be created by just placing the sequence inside the square brackets [].

- **Note-**  Lists are a useful tool for preserving a sequence of data and further iterating over it.

- ###### Adding Elements to a List

  **Using `append()` method**

  Elements can be added to the List by using built-in **`append()`** function. <u>Only one element at a time can be added to the list by using `append()` method, for addition of multiple elements with the `append()` method, loops are used</u>. Tuples can also be added to the List with the use of append method because tuples are immutable. Unlike Sets, Lists can also be added to the existing list with the use of `append()` method.

  **Using `insert()` method**

  `append()` **method only works for addition of elements at the end of the List**, for addition of element at the desired position, `insert() `**method is used. Unlike** `append()` **which takes only one argument, **`insert()` **method requires two arguments(position, value).**

  

  #### Using `extend()` method

  Other than `append()` and `insert()` methods, there’s one more method for Addition of elements, `extend()`, **this method is used to add multiple elements at the same time at the end of the list.**

  

  **Note –** <u>append() and extend() methods can only add elements at the end.</u>

  

## <u>Sets in Python</u>

- **Set** is an unordered collection data type that is **iterable, mutable and has no duplicate elements**. Python’s set class represents the mathematical notion of a set. The major advantage of using a set, as opposed to a list, is that it has a <u>highly optimized method for checking whether a specific element is contained in the set.</u> This is based on a data structure known as a hash table.

- **Frozen sets** in Python are immutable objects that <u>only support methods and operators</u> that produce a result <u>without affecting the frozen set or sets to which they are applied.</u> While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
  If no parameters are passed, it returns an empty frozenset.

- ##### Internal working of Set

  This is based on a data structure known as a hash table.
  <u>If Multiple values are present at the same index position, then the value is appended to that index position, to form a Linked List.</u> In, Python Sets are implemented using dictionary with dummy variables, where key beings the members set with greater optimizations to the time complexity.

  ### <u>Methods for Sets</u>

  ##### Adding elements

  Insertion in set is done through `set.add()` function, where an appropriate record value is created to store in the hash table. Same as checking for an item, i.e., O(1) on average. However, in worst case it can become O(n).

  ##### Union

  Two sets can be merged using union() function or | operator. Both Hash Table values are accessed and traversed with merge operation perform on them to combine the elements, at the same time duplicates are removed. Time Complexity of this is O(len(s1) + len(s2)) where s1 and s2 are two sets whose union needs to be done.

  ##### Intersection

  This can be done through intersection() or & operator. Common Elements are selected. They are similar to iteration over the Hash lists and combining the same values on both the Table. **Time Complexity of this is O(min(len(s1), len(s2))** where s1 and s2 are two sets whose union needs to be done.

  ##### Difference

  To find difference in between sets. Similar to find difference in linked list. This is done through difference() or – operator. **Time complexity of finding difference s1 – s2 is O(len(s1))**

  ##### Clearing sets

  `Clear()` method empties the whole set.

  ##### **There are two major pitfalls in Python sets:**

  1. The set doesn’t maintain elements in any particular order.
  2. Only instances of immutable types can be added to a Python set.



## Time complexity of Sets



|             OPERATION             |     AVERAGE CASE      |                  WORST CASE                   |                   NOTES                    |
| :-------------------------------: | :-------------------: | :-------------------------------------------: | :----------------------------------------: |
|              x in s               |         O(1)          |                     O(n)                      |                                            |
|            Union s\|t             |   O(len(s)+len(t))    |                                               |                                            |
|         Intersection s&t          | O(min(len(s), len(t)) |              O(len(s) * len(t))               | replace “min” with “max” if t is not a set |
| Multiple intersection s1&s2&..&sn |                       | (n-1)*O(l) where l is max(len(s1),..,len(sn)) |                                            |
|          Difference s-t           |       O(len(s))       |                                               |                                            |

## Operators for Sets

Sets and frozen sets support the following operators:

|  OPERATORS   |                      NOTES                       |
| :----------: | :----------------------------------------------: |
|   key in s   |                containment check                 |
| key not in s |              non-containment check               |
|   s1 == s2   |              s1 is equivalent to s2              |
|   s1 != s2   |            s1 is not equivalent to s2            |
|   s1 <= s2   |                s1 is subset of s2                |
|   s1 < s2    |            s1 is proper subset of s2             |
|   s1 >= s2   |               s1 is superset of s2               |
|   s1 > s2    |           s1 is proper superset of s2            |
|   s1 \| s2   |              the union of s1 and s2              |
|   s1 & s2    |          the intersection of s1 and s2           |
|   s1 – s2    |       the set of elements in s1 but not s2       |
|   s1 ˆ s2    | the set of elements in precisely one of s1 or s2 |

#### Python Programs

1. **<u>Anagram</u>**  To check whether two strings are anagrams or not. The strings are assumed to contain only *lower case letters*. The strings are anagrams of each other if the letters of one string can be rearranged to form the other string. So, in anagram strings, all characters occur the same number of times. For example, "ABC" and "CAB" are anagrams, as every character 'A,' 'B,' and 'C' occur the same number of times (one time here) in both the strings.

2. ##### Python: Find duplicates in a list with frequency count & index positions

   ##### Step 1: Get duplicate elements in a list with a frequency count

   Suppose we have a list of strings

   We have created a function that accepts a list and returns a dictionary of duplicate elements in that list along with their frequency count .Let’s call this function to find out the duplicate elements in list with their frequency.

   **What this function is doing?**

   When called, this function creates a new dictionary. Then iterates over all the elements in the given list one by one. For each elements it checks if the element exists in the dictionary keys or not,

   - If element does not exist in dictionary keys, then it adds the element as key in the dictionary with value as 1.
   - If the element exists in dictionary keys, then increments the value of that key by 1.

   Once the iteration of list elements ends, in this dictionary we have the frequency count of each element in the list. But as we are interested in duplicates only i.e. elements with frequency count more than 1. So, it removes the elements from this dictionary whose value is greater than 1. In the end, it returns a dictionary containing duplicate elements as keys and their frequency count as value.

   We can achieve the same using collections.Counter() too,

   ##### Use collections.Counter() Find duplicates in a list with frequency count

   class collections.Counter

   We can create an object of Counter class, using an iterable or any dict like mapping. This Counter object keeps the count of each element in iterable. Let’s use this Counter object to find duplicates in a list and their count.

   Now we know the frequency count of each duplicate element in the list. But what if we want to know the index position of these duplicate elements in the list? Let’s see how to do that,

   ##### Step 2: Get indices of each duplicate element in a list along with frequency count

   Now we want to know indices of each duplicate element in list and also their frequency count. Something like this,

   So, to achieve that we have created a function,

   This function accepts a list of items and then iterates over the items in the list one by one to build a dictionary. In this dictionary, the key will be the element but value will be a list of,

   - Frequency Count
   - List of index positions of elements similar to the given element.

   Let’s call this function to find out the duplicate elements in a list, their index positions, and their frequency.

   **What this function is doing?**

   When we call this function with a list argument, then this function does following steps,

   - First of all, it creates a new dictionary.
   - Then iterates over all the elements in list one by one and keeps the track of index positions.
   - Then for each element, it checks if the element exists in the dictionary keys or not,
     - If element does not exist in dictionary keys then it adds a new key-value pair in dictionary, where the key is the element and value is a list object of 2 items i.e.
       - Frequency count 1
       - List with current index position
     - If the element exists in dictionary keys then it increments the frequency count in the value field and adds the index position in the index list.
   - Once the iteration of list elements finishes, in this dictionary, we have the frequency count of each element in the list, along with index positions.
   - But as we are interested in duplicates only i.e. elements with frequency count more than 1. So, it removes the elements from this dictionary whose value is greater than 1.
   - In the end, it returns a dictionary containing duplicate elements as keys, whereas in value field their frequency count and index positions of duplicate entries.
   
3. ##### Accessing characters by index in string

   In Python indexing of strings starts from 0 till n-1, where n is the size of string. So characters in string of size n, can be accessed from 0 to n-1.

   Suppose we have a string i.e.

   sampleStr = "Hello, this is a sample string"

   Let’s access character at 5th index i.e.

   sampleStr[5]

   We can access and use the character i.e.

   **# Access character at index 5** 

   print( "Character at index 5 is : " , sampleStr[5] )



## Accessing string elements by negative index

We can also access the character in string using negative indexing i.e.

- **string[-1]** will return the last character of string
- **string[-2]** returns the second last character of string
- If string size is n then **string[-n]** will return the first character of string



For Example :

sampleStr = "Hello, this is a sample string"

 print( "Last character in string : " , sampleStr[-1] )

print( "Second Last character in string : " , sampleStr[-2] )

print( "First character in string : " , sampleStr[ -len(sampleStr) ] )

Output:

Last character in string : g 

Second Last character in string : n

First character in string : H