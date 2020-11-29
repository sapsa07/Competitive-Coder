// Maximum sum such that no two elements are adjacent
// Other Forms Kadane's Algorithm - Prefix Sum Array
#include<bits/stdc++.h>
using namespace std;

#define ll long long

int solve(vector<ll> &arr){
	int n = arr.size();
    
    int incl = arr[0]; 
    int excl = 0; 
    int excl_new;
    
    for (int i = 1; i < n; i++) 
    { 
        excl_new = (incl > excl)? incl: excl; 
        
        incl = excl + arr[i]; 
        excl = excl_new; 
    } 
    
    return ((incl > excl)? incl : excl); 	
}

int main(){
	// ...
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    ll n; cin >> n;
    
    vector<ll> v(n);
    
    for(int i=0;i<n;++i)
    {
        ll x; cin >> x;
        v.push_back(x);
    }
    
    ll ans = solve(v);
    cout << ans;   
}