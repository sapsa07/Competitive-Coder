// Largest Number formed from an Array
#include <bits/stdc++.h> 
using namespace std;

int FindMaxNum(int a, int n){
	
}

int main(){
	
	int T;
	int n,a[1000];
	
	while(T--){
		
		cout<<"Enter the Size of an Array :";
		cin>>n;
		
		cout<<"Enter the Elements of an Array :";
		for(int i=0;i<n;i++){
			cin>>a[i];
		}
		
		cout<<"Max. Number of Array :"<<sort(a, a+n);
	}
	
	return 0;
}

