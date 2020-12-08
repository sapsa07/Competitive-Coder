#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    // ...
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
        
    int D1 = 1, V1 = 1, D2 = 1, V2 = 1, P = 1;
    
    int sum = 0, count = 0;
    
    cin >> D1 >> V1 >> D2 >> V2 >> P;
    
    if(D1 == D2){
        while(P == sum){
            sum = sum + (V1+V2);
            count++;
        }
    } else {
        while(P == sum){
            sum = sum + (D1*V1+D2*V2);
            count++;
        }
    }
    
    cout << count;
    
    return 0;
}