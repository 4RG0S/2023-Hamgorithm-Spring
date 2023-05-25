#include <iostream>
using namespace std;

int dp[1001] = {0,1,3};

int d(int n){
    if (dp[n]) return dp[n];

    return dp[n] = (d(n-1) + d(n-2) *2)%10007;
}

int main(){
    int n;
    cin >> n;
    cout << d(n) << endl;

    return 0;
}