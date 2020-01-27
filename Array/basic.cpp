#include<iostream>
using namespace std;

void printArray(int arr[],int n){
	
	for(int i=0;i<n;i++){
			cout<<arr[i] <<"\n";
		}
}

int main(){
	int arr[20],n,T=0;
	
	cout<<"Number of Test Case: ";
	cin>>T;
	
	while(T--){
		cout<<"Enter the Size of Array :";
		cin>>n;
	
		for(int i=0;i<n;i++){
			cout<<"Enter the Elements of Array["<<i<<"] :";
			cin>>arr[i];
		}
		
		printArray(arr,n);
	}
	
	return 0;
}
