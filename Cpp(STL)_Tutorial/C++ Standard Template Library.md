## C++ Standard Template Library

Standard Template Library (STL) is a collection of classes and functions, which is written in the core language. functions like lists, stacks, arrays, etc. The C++ programs in this section deals with the implementation of Standard Template Library like **vectors, maps, set, queue, priority queue, strings, sorting, stacks, arrays, deque, lists, Set_Intersection, Set_Difference, Set_Symmetric_difference, Prev_Permutation and Next_Permutation** in STL.

All the core of the C++ standard template library are the following types 

- Containers

- Algorithms

- Iterators

  

  ### **Containers** 

1. <u>**Vector**</u> - Vector can provide memory flexibility and doesn't needs size during declaration. Vectors are used for creating dynamic arrays of char,integer,float and others. Increase its size by 2^n.

   **Example :** 

   ```c++
   vector<int> v; // Zero Length Vector
   vector<char> v(5); // Creates a 5 element char Vector
   vector<char> cv(4,'a'); // Initialize 4 elements char vector with a
   vector<int> v(5,10); // Initialize 5 elements int vector with 10
   ```

   

2. **Map** - 