#include<iostream>
using namespace std;

int check_prime(int arr[],int n){
	
	int prime_cnt = 0;
	
	     for (int i=0; i<n; i++)
    {
        bool prime=true;
        
        for (int j=2; j*j<=arr[i]; j++)
        {
            if (arr[i] % j == 0)
            {
                prime=false;
                break;
            }
        }   
        if(prime) {
        	cout << arr[i] << " ";
        	prime_cnt++;
		}
    }
	
	return prime_cnt;
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
		
		cout<<"No. of Prime Numbers : "<<check_prime(arr,n)<<"\n";
		
	}
	
	return 0;
}
