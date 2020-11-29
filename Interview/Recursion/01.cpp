// Count ways to reach the nth stair
#include<bits/stdc++.h>
using namespace std;

#define ll long long

void solve(vector<ll> v)
{ 
	
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
	 
	cout<< solve(v); 

	return 0;
}
