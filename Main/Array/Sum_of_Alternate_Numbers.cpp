#include <bits/stdc++.h>

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

    int even = 0; // 0,2,4,6,...
    int odd  = 0; // 1,3,5,7,...

    for (int i = 0; i < n; ++i)
    {
        if (i%2)
            even += v[i];
        else
            odd += v[i];
    }

    cout << "Even :" << even << endl;

    cout << "Odd :" << odd << endl;

    

    return 0;
}

// Idea : Sum of Odd - Even element