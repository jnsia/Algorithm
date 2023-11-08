#include <iostream>
using namespace std;

long long int remains[1000001];
long long int prefix[1000];

int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	int N, M;
	cin >> N >> M;

	int temp;

	for (int i = 1; i < N + 1; i++)
	{
		cin >> temp;
		remains[i] = temp % M;
	}

	for (int i = 1; i < N + 1; i++)
	{
		remains[i] = (remains[i] + remains[i - 1]) % M;
	}

	for (int i = 1; i < N + 1; i++)
	{
		temp = remains[i] % M;
		prefix[temp] += 1;
	}

	long long int answer = prefix[0];

	for (int i = 0; i < M; i++)
	{
		if (prefix[i] > 0) {
			answer += (prefix[i] * (prefix[i] - 1)) / 2;
		}
	}

	cout << answer;

	return 0;
}