// A school method based C++ program to check if a 
// number is prime 
/*
Program to check if a number is prime.
1. checking number less than n to 2 .
2. A optimized of above method .
3. Fermat Method
*/

//1. Basic Method
 
#include <bits/stdc++.h> 
using namespace std; 

bool isPrime(int n) 
{ 
	// Corner case 
	if (n <= 1) return false; 

	// Check from 2 to n-1 (checking number less than n to 2 is divisible if divisible then not prime )
	for (int i=2; i<n; i++) 
		if (n%i == 0) 
			return false; 

	return true; 
} 

int main() 
{ 
	isPrime(11)? cout << " true\n": cout << " false\n"; 
	isPrime(15)? cout << " true\n": cout << " false\n"; 
	return 0; 
} 

// 2. A optimized of above method  

#include <bits/stdc++.h> 
using namespace std; 

bool isPrime(int n) 
{ 
	// Corner cases 
	if (n <= 1) return false; 
	if (n <= 3) return true; 

	// This is checked so that we can skip 
	// middle five numbers in below loop 
	if (n%2 == 0 || n%3 == 0) return false; 

	for (int i=5; i*i<=n; i=i+6) 
		if (n%i == 0 || n%(i+2) == 0) 
		return false; 

	return true; 
} 

int main() 
{ 
	isPrime(11)? cout << " true\n": cout << " false\n"; 
	isPrime(15)? cout << " true\n": cout << " false\n"; 
	return 0; 
} 

//Fermat Method
// C++ program to find the smallest twin in given range 
#include <bits/stdc++.h> 
using namespace std; 

/* Iterative Function to calculate (a^n)%p in O(logy) */
int power(int a, unsigned int n, int p) 
{ 
	int res = 1;	 // Initialize result 
	a = a % p; // Update 'a' if 'a' >= p 

	while (n > 0) 
	{ 
		// If n is odd, multiply 'a' with result 
		if (n & 1) 
			res = (res*a) % p; 

		// n must be even now 
		n = n>>1; // n = n/2 
		a = (a*a) % p; 
	} 
	return res; 
} 

/*Recursive function to calculate gcd of 2 numbers*/
int gcd(int a, int b) 
{ 
	if(a < b) 
		return gcd(b, a); 
	else if(a%b == 0) 
		return b; 
	else return gcd(b, a%b); 
} 

// If n is prime, then always returns true, If n is 
// composite than returns false with high probability 
// Higher value of k increases probability of correct 
// result. 
bool isPrime(unsigned int n, int k) 
{ 
// Corner cases 
if (n <= 1 || n == 4) return false; 
if (n <= 3) return true; 

// Try k times 
while (k>0) 
{ 
	// Pick a random number in [2..n-2]		 
	// Above corner cases make sure that n > 4 
	int a = 2 + rand()%(n-4); 

	// Checking if a and n are co-prime 
	if (gcd(n, a) != 1) 
		return false; 

	// Fermat's little theorem 
	if (power(a, n-1, n) != 1) 
		return false; 

	k--; 
	} 

	return true; 
} 

int main() 
{ 
	int k = 3; 
	isPrime(11, k)? cout << " true\n": cout << " false\n"; 
	isPrime(15, k)? cout << " true\n": cout << " false\n"; 
	return 0; 
} 

