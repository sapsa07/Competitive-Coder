#include<bits/stdc++.h>
using namespace std;

int findCelebrity(int arr, int n)
{
	stack<int> st;
	
	for(int i=0; i<n; i++)
	{
		st.push(i); // Adding All persons 
	}
	
	while(st.size() >= 2)
	{
		int i = st.pop();
		int j = st.pop();
		
		if(arr[i][j] == 1)
		{
			// If i knows j -> i is not a celebrity
			st.push(j);
		} else {
			// if i doesn't know j -> j is not a celebrity
			st.push(i);
		}
	}
	
	int celu = st.pop();
	
	for(int i=0; i<n; i++)
	{
		if(i != celu) // Don't Check the celebrity cell
		{	
			// If 
			if(arr[i][celu] == 0 || arr[celu][i] == 1)
			{
				cout<<"None";
				return;
			}
		}
	}
	
	cout<<celu;
}

int main()
{
	int n; cin>>n; // No. of People
	int arr[n][n];
	
	for(int i=0; i<n; i++)
	{
		for (int j=0; j<n; j++)
		{
			cin >> arr[i][j];
		}
	}
	
	findCelebrity(arr,n);
	
	
}
