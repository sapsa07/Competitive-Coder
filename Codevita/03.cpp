#include<iostream>
#include<math.h>
using namespace std;

int main() {

int a[20][20]; int n;

cin>>n;

for(int i=0;i<n;i++){
	for(int j=0;j<n;j++){
		cin>>a[i][j];
	}
}

for(int i=0;i<n;i++){
	for(int j=0;j<n;j++){
		cout << a[i][j] << " ";
	}
	// Newline for new row 
   cout << endl;
}

return 0;

}
