#include <iostream>

#define ll long long

using namespace std; 
  
int main() 
{
	// ...
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    double pie = 22.0/7; 

	ll d; cin >> d; // no. of days
	ll r;  // radius of circle
	ll x;  // amount of horlicks
	

	int t = 0; // toffee

    while(d--){
		cin >> r >> x;
		
        if(2*pie*r <= 100*x)
            t += 1;
    }

	cout << t << endl;
  
    return 0; 
}