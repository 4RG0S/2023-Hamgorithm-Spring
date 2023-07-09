#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct info_flower {
    pair<int, int> bloom;
    pair<int, int> fall;
};

bool comp_flower(info_flower A, info_flower B) {
    if (A.bloom.first == B.bloom.first) {
        if (A.bloom.second == B.bloom.second) {
            if (A.fall.first == B.fall.second)
                return A.fall.second < B.fall.second;
            else
                return A.fall.first < B.fall.first;
        }
        else
            return A.bloom.second < B.bloom.second;
    }
    else
        return A.bloom.first < B.bloom.first;
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<info_flower> flower(n);
    for (int i = 0; i < n; i++) {
        cin >> flower[i].bloom.first >> flower[i].bloom.second;
        cin >> flower[i].fall.first >> flower[i].fall.second;
    }
    sort(flower.begin(), flower.end(), comp_flower);

    int i = 0;
    int tot = 0;
    pair<int, int> bigtime(0, 0);
    pair<int, int> lasttime(3, 1);
    
    while (true) {
        for (; i < n; i++) {
            if (flower[i].bloom > lasttime)
                break;
            if (flower[i].fall > bigtime)
                bigtime = flower[i].fall;
        }
        if (bigtime == make_pair(0, 0)) {
            tot = 0;
            break;
        }
        if (bigtime >= make_pair(11, 31)) {
            tot++;
            break;
        }
        lasttime = bigtime;
        bigtime = make_pair(0, 0);
        tot++;
    }

    cout << tot;

    return 0;
}