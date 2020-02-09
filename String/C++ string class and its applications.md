# C++ string class and its applications

In C++ we can store string by one of the two ways –

1. C style strings
2. String class

In this post, the second method is discussed. string class is part of C++ library that supports a lot much functionality over C style strings.

**C++ string** class internally uses **char array to store character** but all memory management, allocation, and null termination is handled by string class itself that is why it is easy to use.

<u>The length of the C++ string can be changed at runtime because of dynamic allocation of memory similar to vectors.</u>

As string class is a container class, we can iterate over all its characters using an iterator similar to other containers like vector, set and maps, but generally, we use a simple for loop for iterating over the characters and index them using [] operator.