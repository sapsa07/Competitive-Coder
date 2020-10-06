# Cpp STL

#### Binary Search

**Sort the Array --> Do binary Search**

Binary search is a widely used searching algorithm that requires the array to be sorted before search is applied. 

The main idea behind this algorithm is to keep dividing the array in half (divide and conquer) until the element is found, or all the elements are exhausted.

It works by comparing the middle item of the array with our target, if it matches, it returns true otherwise if the middle term is greater than the target, the search is performed in the left sub-array.
If the middle term is less than target, the search is performed in the right sub-array.

The prototype for binary search is :

```cpp
binary_search(startaddress, endaddress, valuetofind)

**startaddress: the address of the first element of the array.**
**endaddress: the address of the last element of the array.**
**valuetofind: the target value which we have to search for.**


```

