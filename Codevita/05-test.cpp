#include<iostream>
#include<vector>
using namespace std;

int main(){
	
	vector<int> v1;
	int ele,n;
	
	cin>>n;
	
	vector<int> :: iterator it = v1.begin();
	
	for(int i=0;i<n ;i++){
		cin>>ele;
		v1.push_back(ele);
	}
	
	for(int i=0;i<n ;i++){
		cout<<"Numbers : "<<v1[i]<<endl;
	}
	
	return 0;
}
