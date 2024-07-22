#include <iostream>
using namespace std;

int matrix[101][101];

int main(void) {
	int N, M, temp;
	cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++) {
			cin >> matrix[i][j];
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++) {
			cin >> temp;
			matrix[i][j] += temp;
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++) {
			cout << matrix[i][j] << " ";
		}

		cout << endl;
	}

	return 0;
}