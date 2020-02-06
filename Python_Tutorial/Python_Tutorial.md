# 						**Python Tutorial**



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

  



#### **Python Arrays**

Python has 3 main sequence classes:

- List : [1,2,3]
- Tuple : (1,2,3)
- String : '123'

All support indexing (**e.g.** t[0] = 1) 



#### **Python Programs**

1. **<u>Anagram</u>**  To check whether two strings are anagrams or not. The strings are assumed to contain only *lower case letters*. The strings are anagrams of each other if the letters of one string can be rearranged to form the other string. So, in anagram strings, all characters occur the same number of times. For example, "ABC" and "CAB" are anagrams, as every character 'A,' 'B,' and 'C' occur the same number of times (one time here) in both the strings.

2. 