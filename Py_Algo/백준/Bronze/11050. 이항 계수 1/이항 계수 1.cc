#include <iostream>
using namespace std;

long factorial[11];

int main(void) {

	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

	int N, K;
	cin >> N >> K;

	// N! / (N - K)! * (K)!

	factorial[1] = 1;

	for (int i = 2; i < 11; i++)
	{
		factorial[i] = i * factorial[i - 1];
	}

	if (N == K || K == 0) {
		cout << 1;
	}
	else {
		cout << factorial[N] / (factorial[N - K] * factorial[K]);
	}

    return 0;
}