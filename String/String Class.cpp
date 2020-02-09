// C++ program to demonstrate various function string class 
#include <bits/stdc++.h> 
using namespace std; 

int main() 
{ 
	
	/*
	
	int n; 
	cin>>n;
	
	for(int i=0;i<n;i++){
		cin>>str1;
	}
	for(int i=0;i<n;i++){
		cout<<str1;
	} 
	
	output : eeeee
	*/
	
	// initialization by raw string 
	string str1("ABCDEFGH"); 

	// initialization by another string 
	string str2(str1); 

	// initialization by character with number of occurrence 
	string str3(5, '#'); 

	// initialization by part of another string 
	string str4(str1, 6, 6); // from 6th index (second parameter) 6 characters (third parameter) 

	// initialization by part of another string : iteartor version 
	string str5(str2.begin(), str2.begin() + 5); 

	cout << "str1 " << str1 << endl; 
	cout << "str2 " << str2 << endl; 
	cout << "str3 " << str3 << endl; 
	cout << "str4 "<< str4 << endl; 
	cout << "str5 "<< str5 << endl; 

	return 0; 
} 

