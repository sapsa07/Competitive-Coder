## 

1. Consecutive Prime Sum



Some prime numbers can be expressed as a sum of other consecutive prime numbers. For example 5 = 2 + 3, 17 = 2 + 3 + 5 + 7, 41 = 2 + 3 + 5 + 7 + 11 + 13. Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.

Write code to find out the number of prime numbers that satisfy the above-mentioned property in a given range.



![tcs codevita questions from previous year](https://i1.faceprep.in/fp/articles/img/54653_1580292063.png)



**Input Format:** First line contains a number N

**Output Format:** Print the total number of all such prime numbers which are less than or equal to N.

**Constraints:** 2<N<=12,000,000,000



Q2

## **Bank Compare**

There are two banks – Bank A and Bank B. Their interest rates vary. You have received offers from both banks in terms of the annual rate of interest, tenure, and variations of the rate of interest over the entire tenure.

You have to choose the offer which costs you least interest and reject the other. Do the computation and make a wise choice.

The loan repayment happens at a monthly frequency and Equated Monthly Installment (EMI) is calculated using the formula given below :

EMI = loan Amount * monthly Interest Rate / ( 1 – 1 / (1 + monthly Interest Rate)^(number Of Years * 12))

**Constraints:**

1 <= P <= 1000000

1 <=T <= 50

1<= N1 <= 30

1<= N2 <= 30



**Input Format:**

- First line: P principal (Loan Amount)
- Second line: T Total Tenure (in years).
- Third Line: N1 is the number of slabs of interest rates for a given period by Bank A. First slab starts from the first year and the second slab starts from the end of the first slab and so on.
- Next N1 line will contain the interest rate and their period.
- After N1 lines we will receive N2 viz. the number of slabs offered by the second bank.
- Next N2 lines are the number of slabs of interest rates for a given period by Bank B. The first slab starts from the first year and the second slab starts from the end of the first slab and so on.
- The period and rate will be delimited by single white space.

**Output Format:** Your decision either Bank A or Bank B.

**Explanation:**

Example 1

Input

10000

20

3

5 9.5

10 9.6

5 8.5

3

10 6.9

5 8.5

5 7.9

**Output**: Bank B



Example 2

Input

500000

26

3

13 9.5

3 6.9

10 5.6

3

14 8.5

6 7.4

6 9.6

**Output**: Bank A