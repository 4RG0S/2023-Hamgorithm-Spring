#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    int idx;
    string table = "abcdefghijklmnopqrstuvwxyz";

    cin >> s;
    
    for(int i = 0; i < table.length(); i++){
        idx = s.find(table[i]);

        if (idx < 0){
            cout << -1 << " ";
        }
        
        else{
            cout << idx << " ";
        }
        
    }
    
    return 0;
}