#include <iostream>
#include <map>
#include <string>
#include <sstream>

using namespace std;

int main() {

    int n, m;
    cin >> n >> m;
    
    map<string, string> book;
    string url, pwd;

    for (int i=0; i<n; i++) {
        cin >> url >> pwd;
        book.insert(make_pair(url, pwd));
    }

    for (int i=0; i<m; i++) {
        cin >> url;
        auto a = book.find(url);
        cout << a->second << '\n';
    
    }
        

    return 0;
}