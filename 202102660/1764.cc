#include <iostream>
#include <algorithm>
#include <string>

#define MAXLEN 500000
using namespace std;

string no_hear[MAXLEN];
string no_see[MAXLEN];
string no_sh[MAXLEN];

int main() {
    int N, M, count=0;
    cin >> N >> M;
    
    for (int i=0; i < N; i++) {
        cin >> no_hear[i];
    }
    for (int i=0; i < M; i++) {
        cin >> no_see[i];
    }
    
    sort(no_hear, no_hear+N);
    
    for(int i=0; i<M; i++) {
        if(binary_search(no_hear, no_hear+N, no_see[i])) {
            no_sh[count] = no_see[i];
            count++;
        }
    }
    sort(no_sh, no_sh+count);

    cout << count << '\n';

    for(int i=0; i<count; i++) {
        cout << no_sh[i] <<'\n';
    }

    return 0;
}