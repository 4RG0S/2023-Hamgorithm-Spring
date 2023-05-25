#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Ball {
    int idx;
    int color;
    int size;
};

bool comp_ballsize(Ball a, Ball b) {
    if (a.size == b.size)
        return a.color < b.color;
    else
        return a.size < b.size;
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<Ball> ball(n);
    for (int i = 0; i < n; i++) {
        ball[i].idx = i;
        cin >> ball[i].color;
        cin >> ball[i].size;
    }
    sort(ball.begin(), ball.end(), comp_ballsize);

    vector<int> sum_ballsize(n);
    vector<int> sum_colorball(n + 1, 0);
    vector<int> correct(n);
    int samesizecount = 0;
    int samecolorcount = 0;

    correct[ball[0].idx] = 0;
    sum_ballsize[0] = ball[0].size;
    sum_colorball[ball[0].color] = ball[0].size;

    for (int i = 1; i < n; i++) {
        if (ball[i].size == ball[i - 1].size) {
            samesizecount++;

            if (ball[i].color == ball[i - 1].color)
                samecolorcount++;
            else
                samecolorcount = 0;
        }
        else {
            samesizecount = 0;
            samecolorcount = 0;
        }


        correct[ball[i].idx] = sum_ballsize[i - 1] - sum_colorball[ball[i].color] - ball[i].size * samesizecount + ball[i].size * samecolorcount;

        sum_ballsize[i] = ball[i].size + sum_ballsize[i - 1];
        sum_colorball[ball[i].color] += ball[i].size;
    }

    for (int i = 0; i < n; i++)
        cout << correct[i] << '\n';

    return 0;
}