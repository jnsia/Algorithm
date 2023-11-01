#include <iostream>
using namespace std;

int dp[41];

int main()
{
	int N;
	cin >> N;

	dp[1] = 1;
	dp[2] = 1;

	for (int i = 3; i < 41; i++)
	{
		dp[i] = dp[i - 1] + dp[i - 2];
	}

	cout << dp[N] << " " << N - 2;
}
