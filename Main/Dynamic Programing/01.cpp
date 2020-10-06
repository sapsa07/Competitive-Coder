// 01 Knapsack Problem
#include<iostream>
using namespace std;

int knapSack(int W, int wt[], int val[], int n) {
  

}


// Driver code
int main()
{
    int val[] = { 60, 100, 120 }; // Value of Each Item
    int wt[] = { 10, 20, 30 }; // Weight of Each Item
    int W = 50; // Maximum Capacity of Bag

    int n = sizeof(val) / sizeof(val[0]);

    cout << knapSack(W, wt, val, n);
    return 0;
}
