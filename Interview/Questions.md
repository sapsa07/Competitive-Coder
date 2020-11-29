1. Find missing number in an array using XOR based method.

   **Complexity Analysis:** 

   - **Time Complexity:** O(n) + O(n) = O(2n) = **O(n)** 
     Only one traversal of the array is needed
   - **Space Complexity:** O(1)
     No extra space is needed

   - Approach:

     XOR has certain properties 

     - Assume a1 ^ a2 ^ a3 ^ …^ an = a **and** a1 ^ a2 ^ a3 ^ …^ an-1 = b
     - Then a ^ b = an

   - Algorithm:

     1. Create two variables *a = 0* and *b = 0*
     2. Run a loop from 1 to n with i as counter.
     3. For every index update *a* as *a = a ^ i*  - to get xor value of all the *n* natural numbers
     4. Now traverse the array from start to end.
     5. For every index update *b* as *b = b ^ array[i]* - to get xor value of all the elements in the array
     6. Print the missing number as *a ^ b*.

   - Example

     - [1,2,4,5,6]
     - (1^2^4^5^6) ^ (1^2^3^4^5^6) = 4 ^ 7 = 3

2. Finding middle node in a linked list in O(N) time and in single pass

   1. Naive Approach -  To count the size of the linked list and divide the size by two to get the middle element.
   2. Two Pointer



**DP**

1. **Count ways to reach the n’th stair**

   There are n stairs, a person standing at the bottom wants to reach the top. 

   The person can climb either 1 stair or 2 stairs at a time. 

   Count the number of ways, the person can reach the top.

   *

   