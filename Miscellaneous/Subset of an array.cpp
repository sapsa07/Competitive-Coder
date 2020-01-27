// Find Subset of an array (Power Set)
#include<iostream>
#include<math.h>
using namespace std;

int power_set(char *set, int set_size){
	
	int pow_set_size = pow(2,set_size);
	int counter,j;
	
	cout << "Subsets are :"; 
	
	/*Run from counter 000..0 to 111..1*/
    for(counter = 0; counter < pow_set_size; counter++) 
    { 
	    for(j = 0; j < set_size; j++) 
	    { 
	        //Check if jth bit in the counter is set.If set then print jth element from set
	        if(counter & (1 << j)) // counter is used bcoz if counter = 0 then its null
	            cout << set[j]; 
	    } 
    cout << endl; 
    } 
}


int main(){
	
	char set[10]; int n;
	
	cout<<"Enter Set Size :"; cin>>n;
	
	cout<<"Enter Set Values :";
	for(int i=0; i<n;i++){
		cin>>set[i];
	}
	
	power_set(set,n);
	
	return 0;
}
