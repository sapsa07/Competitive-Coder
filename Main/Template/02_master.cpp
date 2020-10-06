#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
//#include <bits/stdc++.h>

#define ll long long

using namespace std;

int main()
{
    // ...
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n; cin >> n;
    vector<ll> v;
    
    for(int i=0;i<n;i++)
    {
        ll x; cin >> x;
        v.push_back(x);
    }
    
    // sort(v.begin(),v.end());
    
    return 0;
}