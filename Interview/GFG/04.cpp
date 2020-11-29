// You are given a list of n-1 integers and these integers are in the range of 1 to n. 
// No duplicates in the list. One of the integers is missing in the list. Find the missing one. XOR Based Solution
#include<bits/stdc++.h>
using namespace std;

#define ll long long

int solve(vector<ll> &arr){
	int n = arr.size(); // Vector Size
	
	// For xor of all the elements in array
    int x1 = arr[0];
 
    // For xor of all the elements from 1 to n+1
    int x2 = 1;
 
    for (int i = 1; i < n; i++)
        x1 = x1 ^ arr[i];
 
    for (int i = 2; i <= n + 1; i++)
        x2 = x2 ^ i;
 
    return (x1 ^ x2);
}

int main(){
	// ...
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    ll n; cin >> n;
    
    vector<ll> v;
    
    for(int i=0;i<n;++i)
    {
        ll x; cin >> x;
        v.push_back(x);
    }
    
    int miss = solve (v);
    cout << "miss :" << miss << endl;
    
}
