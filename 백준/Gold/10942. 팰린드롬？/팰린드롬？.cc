#include <iostream>
using namespace std;

int N, M;
int arr[2001];
short dp[2001][2001];

int main(void) {

	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

	cin >> N;

	for (int i = 1; i < N + 1; i++)
	{
		cin >> arr[i];
	}

	for (int i = 1; i < N + 1; i++)
	{
		dp[i][i] = 1;
	}

	for (int i = 1; i < N; i++)
	{
		if (arr[i] == arr[i + 1]) dp[i][i + 1] = 1;
	}

	for (int i = 2; i < N; i++)
	{
		for (int j = 1; j < N - i + 1; j++) {
			if (arr[j] == arr[j + i] && dp[j + 1][j + i - 1] == 1) {
				dp[j][j + i] = 1;
			}
		}
	}

	cin >> M;

	int S, E;

	for (int i = 0; i < M; i++)
	{
		cin >> S >> E;

		cout << dp[S][E] << "\n";
	}

    return 0;
}