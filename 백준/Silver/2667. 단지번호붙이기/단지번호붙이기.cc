#include <iostream>
#include <algorithm>
using namespace std;

int N, cnt, apart_cnt, nx, ny;
char input[26];
int apart[626];
int matrix[26][26];
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

int dfs(int x, int y) {
	cnt += 1;

	for (int move = 0; move < 4; move++)
	{
		nx = x + dx[move];
		ny = y + dy[move];

		if ((nx >= 0 || nx < N) && (ny >= 0 || ny < N) && (matrix[nx][ny] == 1)) {
			matrix[nx][ny] = 0;
			dfs(nx, ny);
		}
	}

	return 0;
}

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> input;

		for (int j = 0; j < N; j++)
		{
			matrix[i][j] = int(input[j]) - int('0');
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (matrix[i][j] == 1) {
				cnt = 0;
				matrix[i][j] = 0;
				dfs(i, j);
				apart[apart_cnt] = cnt;
				apart_cnt += 1;
			}
		}
	}

	sort(apart, apart + apart_cnt);

	cout << apart_cnt << "\n";

	for (int i = 0; i < apart_cnt; i++)
	{
		cout << apart[i] << "\n";
	}
}