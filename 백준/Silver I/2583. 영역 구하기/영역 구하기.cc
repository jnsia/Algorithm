#include <iostream>
#include <algorithm>
using namespace std;

int M, N, K;
int paper[101][101];
int answer = 0;
int temp;
int result[10000];
int result_size = 0;

int dx[] = { 1, 0, -1, 0 };
int dy[] = { 0, 1, 0, -1 };

void dfs(int x, int y) {
	temp += 1;

	int nx, ny;

	for (int i = 0; i < 4; i++)
	{
		nx = x + dx[i];
		ny = y + dy[i];

		if (nx >= 0 && nx < M && ny >= 0 && ny < N && paper[nx][ny] == 0) {
			paper[nx][ny] = 1;
			dfs(nx, ny);
		}
	}
}

int main(void) {
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

	cin >> M >> N >> K;

	for (int i = 0; i < K; i++)
	{
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;

		for (int j = x1; j < x2; j++)
		{
			for (int k = y1; k < y2; k++)
			{
				paper[k][j] = 1;
			}
		}
	}

	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (paper[i][j] == 0) {
				answer++;
				paper[i][j] = 1;
				temp = 0;
				dfs(i, j);
				result[result_size++] = temp;
			}
		}
	}

	sort(result, result + result_size);

	cout << answer << "\n";
	
	for (int i = 0; i < result_size; i++)
	{
		cout << result[i] << " ";
	}

    return 0;
}