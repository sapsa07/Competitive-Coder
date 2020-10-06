#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>

#define ll long long

using namespace std; 
  
int main() 
{
	// ...
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    ll n; cin >> n;
    vector<ll> v;
    
    for(int i=0;i<n;i++)
    {
        ll x; cin >> x;
        v.push_back(x);
    }
    
    // ... Print ...
	for(ll i = 0; i < v.size(); ++i) 
        cout << v[i] << " ";
  
    return 0; 
}