#include <iostream>
using namespace std;

#define min(x, y) ((x > y) ? (y) : (x))

int prefix[2001][2001];

int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	int N, M, K;
	cin >> N >> M >> K;
	char c;

	int BW[2] = { 'B', 'W' };

	for (int i = 1; i < N + 1; i++)
	{
		for (int j = 1; j < M + 1; j++)
		{
			cin >> c;
			int temp = (i + j) % 2;
		
			if (c == BW[temp]) {
				prefix[i][j] = 1;
			}
		}
	}

	for (int i = 1; i < N + 1; i++)
	{
		for (int j = 1; j < M + 1; j++)
		{
			prefix[i][j] += prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1];
		}
	}

	int max_count = K * K;
	int answer = K * K;

	for (int i = K; i < N + 1; i++)
	{
		for (int j = K; j < M + 1; j++)
		{
			int temp = prefix[i][j] - prefix[i - K][j] - prefix[i][j - K] + prefix[i - K][j - K];
			temp = min(temp, max_count - temp);
			answer = min(answer, temp);
		}
	}

	cout << answer;

	return 0;
}