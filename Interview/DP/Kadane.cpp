// Kadane's Algorithm
#include<bits/stdc++.h>
using namespace std;

#define ll long long

int solve(vector<ll> &arr){
	int n = arr.size(); // Array Size

    int csum = INT_MIN, max_sum = 0; 
  
    for (int i = 0; i < n; i++) 
    { 
        max_sum = max_sum + arr[i];

        if (csum < max_sum) 
            csum = max_sum; 
  
        if (max_sum < 0) 
            max_sum = 0; 
    }
    
    return csum; 
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
