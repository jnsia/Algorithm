#include <iostream>
using namespace std;

int matrix[1025][1025];

int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	int N, M;
	cin >> N >> M;

	for (int i = 1; i < N + 1; i++)
	{
		for (int j = 1; j < N + 1; j++) {
			cin >> matrix[i][j];
		}
	}

	for (int i = 1; i < N + 1; i++)
	{
		for (int j = 1; j < N + 1; j++) {
			matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1];
		}
	}

	int x1, y1, x2, y2;

	for (int i = 0; i < M; i++)
	{
		cin >> x1 >> y1 >> x2 >> y2;

		cout << matrix[x2][y2] - matrix[x2][y1 - 1] - matrix[x1 - 1][y2] + matrix[x1 - 1][y1 - 1] << "\n";
	}

	return 0;
}