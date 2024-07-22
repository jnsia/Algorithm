#include <iostream>
using namespace std;

#define min(x, y) ((x > y) ? (y) : (x))

int main() {
	int N, M;
	cin >> N >> M;

	char WB[2] = { 'W', 'B' };
	char chess[51][51];

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> chess[i][j];
		}
	}

	int answer = 64;

	for (int i = 0; i <= N - 8; i++)
	{
		for (int j = 0; j <= M - 8; j++)
		{
			int count = 0;

			for (int k = i; k < i + 8; k++)
			{
				for (int l = j; l < j + 8; l++)
				{
					if (WB[(k + l) % 2] == chess[k][l]) {
						count += 1;
					}
				}
			}

			answer = min(answer, min((64 - count), count));
		}
	}

	cout << answer;

	return 0;
}