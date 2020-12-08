// VACCINE2
#include<bits/stdc++.h>
using namespace std;

#define ll long long int

int main(){
	ll t; cin >> t;
	while(t--){
		ll n,d;
		cin >> n >> d;

		vector<ll> v;
		ll risk=0, norisk=0;
    
	    for(int i=0;i<n;i++)
	    {
	        ll x; cin >> x;
	        v.push_back(x);

	        if (v[i] >= 80 || v[i] <= 9) risk++;
	        else norisk++;


	    }
	    
	     ll sum= ceil((double)risk / (double)d) + ceil((double)norisk / (double)d);

	     cout<<sum<<"\n";
	}

	return 0;
}