#include <bits/stdc++.h>

#define ll long long

using namespace std;

int maxSubArraySum(int v[],int n)
{
    int max_far = INT_MIN; // Maximum Sum

    int max_here = 0; // Maximum till now 

    for (int i = 0; i < n; ++i)
    {
        max_here += v[i];

        if (max_far < max_here)
         {
            max_far = max_here;
         } 

         if (max_here < 0)
         {
            max_here = 0;
         }
    }

    return max_far;
}

int main()
{
    // ...
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n; cin >> n;
    int v[n];
    
    for(int i=0;i<n;i++)
    {
        cin >> v[i];
    }
    
    int max_sum = maxSubArraySum(v,n);

    cout << "Maximum Sum is :" << max_sum;
    
    return 0;
}

// Complexity - O(n)
// Idea : To Look for all positive contiguous segment of the array