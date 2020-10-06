#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>

#define ll long long

using namespace std;

int gcd(int a, int b)
{
    // Everything divides 0
    if (a == 0)
    {
        return b;
    }

    if (b == 0)
    {
        return a;
    }

    // base case
    if (a == b)
    {
        return a;
    }

    return gcd(b % a, a);
}
  
int main() 
{
	cout << gcd(4,2);
  
    return 0; 
}