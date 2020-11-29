#include<bits/stdc++.h>
using namespace std;

#define ll long long

int solve(vector<ll> &arr){
	int s = arr.size(); // Vector Size
	
	ll left[s], right[s];
	
	left[0] = 1;
	
	for(int i=1; i<s; i++){
		if(arr[i] <= arr[i-1]){
			left[i] = 1;
		}
		else{
			left[i] = left[i-1] + 1;
		}
	}
	
	right[s-1] = 1;
	
	for(ll i = s - 2; i>=0;i--){
		if(arr[i] <= arr[i+1])
	    {
	    	right[i] = 1;
	    }
	    else{
	        right[i] = right[i+1]+1;
	    }
	}
		
	
	ll answer = 0;
    for(ll i=0; i<s; i++)
    {
       answer+=max(right[i],left[i]);
    }

    return answer;
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
    
    cout << solve (v) << endl;
    
    
}
