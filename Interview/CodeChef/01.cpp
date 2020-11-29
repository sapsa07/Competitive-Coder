#include<bits/stdc++.h>
using namespace std;

#define ll long long

void solve(vector<ll> v, ll q, ll r)
{ 
	ll n = v.size(); // Vector Size
	const ll mod = 10^9 + 7;


} 

int main() 
{ 
	int t; cin >> t;
	while(t--){
		ll n; cin >> n;
		vector<ll> v; 

		for (ll i = 0; i < n; ++i) 
		{ 
			ll x; cin >> x;
			v.push_back(x); 
		}

		ll q; cin >> q; // 
		ll r; cin >> r; // Query

		 
		cout<< solve(v,q,r);
	} 

	return 0;
}