// Reverse given string using Recursion
#include <iostream>
#include <algorithm>
using namespace std;

// Note string is passed as reference parameter
void reverse(string &str, int k)
{
	static int i = 0;

	// if we have reached the end of the string
	if (k == str.length())
		return;

	reverse(str, k + 1);

	if (i <= k)
		swap(str[i++], str[k]);
}


int main()
{
	string str = "Techie Delight";

	reverse(str, 0);
	cout << "Reverse of the given string is : " << str;

	return 0;
}
