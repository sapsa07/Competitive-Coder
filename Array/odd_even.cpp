#include<iostream>
using namespace std;

int check_even(int arr[],int n){
	
	int even_cnt = 0,odd_cnt=0;
	
	for(int i=0;i<n;i++){
		if(arr[i]%2==0){
			even_cnt++;
		}
		else{
			odd_cnt++;
		}
	}
	
	return even_cnt;
}

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
		
		cout<<"Enter No. of Even Numbers : "<<check_even(arr,n)<<"\n";
		
	}
}
