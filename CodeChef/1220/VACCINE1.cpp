// VACCINE1
// DEC20B
#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    // ...
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
        
    int D1 = 1, V1 = 1, D2 = 1, V2 = 1, P = 1, i, sum = 0;
    
    cin >> D1 >> V1 >> D2 >> V2 >> P;
    
    for(i=1;i<=10000;i++)
    {
    	if(D1<=i) sum+=V1;

    	if(D2<=i) sum+=V2;

    	if(sum>= P) break;
    }

    cout << i;
    
    return 0;
}