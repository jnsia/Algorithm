#include <iostream>
using namespace std;

#define max(x, y) ((x > y) ? (x) : (y))

int days[100001];

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	int N, K;
	cin >> N >> K;

	for (int i = 1; i < N + 1; i++)
	{
		cin >> days[i];
		days[i] += days[i - 1];
	}

	int answer = -10000001;

	for (int i = K; i < N + 1; i++)
	{
		int temp = days[i] - days[i - K];
		answer = max(answer, temp);
	}

	cout << answer;

	return 0;
}