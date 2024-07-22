#include <iostream>
#include <algorithm>
using namespace std;

int N, M, x, y, nx, ny, queue_size;
int tomato[1000001][2];
int matrix[1001][1001];
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

int bfs() {
	int idx = 0;

	while (idx < queue_size) {
		x = tomato[idx][0];
		y = tomato[idx][1];
			
		for (int move = 0; move < 4; move++)
		{
			nx = x + dx[move];
			ny = y + dy[move];

			if ((nx >= 0 && nx < M) && (ny >= 0 && ny < N) && (matrix[nx][ny] == 0)) {
				matrix[nx][ny] = matrix[x][y] + 1;
				tomato[queue_size][0] = nx;
				tomato[queue_size][1] = ny;
				queue_size += 1;
			}
		}
		idx += 1;
	}

	short is_done = 1;
	int max_time = 0;

	for (int i = 0; i < M; i++)
	{
		if (is_done == 0) break;

		for (int j = 0; j < N; j++)
		{
			if (matrix[i][j] == 0) {
				max_time = 0;
				is_done = 0;
				break;
			}

			if (matrix[i][j] > max_time) {
				max_time = matrix[i][j];
			}
		}
	}

	return max_time - 1;
}

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int temp;

	cin >> N >> M;

	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> temp;
			matrix[i][j] = temp;

			if (temp == 1) {
				tomato[queue_size][0] = i;
				tomato[queue_size][1] = j;

				queue_size += 1;
			}

		}
	}

	cout << bfs();
}