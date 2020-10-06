// Binary Search Using Vector of pairs
#include <bits/stdc++.h> 
using namespace std;

int main() 
{
	// ...
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n; cin >> n;
    vector<int> v;
    
    for(int i=0;i<n;i++)
    {
        int x; cin >> x;
        v.push_back(x);
    }

	// sorting the vector
	sort(v.begin(), v.end());

	// Key
	int key; cin >> key;


	// searching for the key element
	if (binary_search(v.begin(), v.end(), key))
		cout << "Element found"; 
	else
		cout << "Element not found";

	return 0; 
} 
