#include <stdio.h>
#include <string.h>

int r, c;
char v[10][11], vt[10][10][4];

void dfs(int rr, int cc, int pr, int pc, int d) {
	if (0 > rr || r <= rr || 0 > cc || c <= cc || vt[rr][cc][d] || v[rr][cc] == 'X') return;
	vt[rr][cc][d] = 1;
	if (pr != rr - 1 || pc != cc) dfs(rr - 1, cc, rr, cc, 0);
	if (pr != rr || pc != cc + 1) dfs(rr, cc + 1, rr, cc, 1);
	if (pr != rr + 1 || pc != cc) dfs(rr + 1, cc, rr, cc, 2);
	if (pr != rr || pc != cc - 1) dfs(rr, cc - 1, rr, cc, 3);
}

int detect(int rr, int cc) {
	int i, j;
	memset(vt, 0x00, sizeof(vt));
	dfs(rr - 1, cc, rr, cc, 0);
	dfs(rr, cc + 1, rr, cc, 1);
	dfs(rr + 1, cc, rr, cc, 2);
	dfs(rr, cc - 1, rr, cc, 3);
	for (i = 0; i < 4; i++)
		if (vt[rr][cc][i]) return 0;
	return 1;
}

int wallCount(int rr, int cc) {
	int cnt = 0;
	if (v[rr][cc] == 'X') return 0;
	if (rr - 1 < 0 || v[rr - 1][cc] == 'X') cnt++;
	if (rr + 1 >= r || v[rr + 1][cc] == 'X') cnt++;
	if (cc - 1 < 0 || v[rr][cc - 1] == 'X') cnt++;
	if (cc + 1 >= c || v[rr][cc + 1] == 'X') cnt++;
	return cnt;
}

int main(void) 
{
	int i, j;

	scanf("%d %d", &r, &c);
	for (i = 0; i < r; i++) scanf("%s", v[i]);

	for (i = 0; i < r; i++) {
		for (j = 0; j < c; j++) {
			if (wallCount(i, j) >= 3 || (v[i][j] == '.' && detect(i, j))) {
				printf("1\n");
				return 0;
			}
		}
	}
	printf("0\n");
	return 0;
}