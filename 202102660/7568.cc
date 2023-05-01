#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

vector<tuple<int, int, int, int>> v;
int arr[50];

int main() {
    int n=0, a=0, b=0, count=0;
    cin >> n;

    for (int i=0; i<n; i++) {
        // cout <<"!";
        cin >> a >> b;

        v.push_back(make_tuple(i+1, a, b, count));
    }

    for (int i = 0; i < n; i++) {
        count = 1;
        for (int j = 0; j < n; j++){
            if (i != j) {
                if ((get<1>(v[i]) < get<1>(v[j])) && (get<2>(v[i]) < get<2>(v[j]))) {
                    count++;
                }
            }
        
        }
        v[i] = make_tuple(get<0>(v[i]), get<1>(v[i]), get<2>(v[i]), count);

    }
    for (int i=0; i<n; i++) {
        arr[get<0>(v[i])-1] = get<3>(v[i]);
    }
    for (int i=0; i<n; i++) {
        cout << arr[i] << " ";
    }
    cout << '\n';
    
    return 0;
}
