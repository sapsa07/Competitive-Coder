// Alternate Position of Array
// Sum of even and odd elements in an array
#include<bits/stdc++.h>
using namespace std;

#define ll long long

void solve(vector<ll> &arr)
{
	int n = arr.size();

	int odd = 0, even = 0;

	for (int i = 0; i < n; ++i)
	{
		if(i%2 == 0){
			even = even + arr[i];
		}
		else{
			odd = odd + arr[i];
		}
	}

	cout << " o :" << odd << "e :" << even;
} 

int main() 
{ 
	ll n; cin >> n;
	vector<ll> v;

	for (ll i = 0; i < n; ++i) 
	{ 
		ll x; cin >> x;
		v.push_back(x); 
	}
	 
	solve(v); 

	return 0;
}
