// maximum and Minimum elements from the array.
#include<iostream>
#include <climits>
#include <algorithm>
using namespace std;

int main(){
	int arr[100],n,T=0, i, max, min;
	
	cout<<"Number of Test Case: ";
	cin>>T;
	
	while(T--){
		
    cout << "Enter the size of the array : ";
    cin >> n;
    
    cout << "Enter the elements of the array : ";
    for (i = 0; i < n; i++)
        cin >> arr[i];

    max = arr[0];
    for (i = 0; i < n; i++)
    {
        if (max < arr[i])
            max = arr[i];
    }
    
    min = arr[0];
    for (i = 0; i < n; i++)
    {
        if (min > arr[i])
            min = arr[i];
    }
    cout << "\nLargest element : " << max <<" Smallest element : " << min;	
	}
	
	return 0;
}

