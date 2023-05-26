#include <iostream>

using namespace std;

int main(){
    int a, b, c, result;
    int num;
    int num_table[10] = {0, };

    cin >> a >> b >> c;

    result = a * b * c;
    
    while (result > 0){
        num = result % 10;
        num_table[num]++;
        result /= 10;
    }

    for (int i = 0; i < 10; i++){
        cout << num_table[i] << endl;
    }

    return 0;
}