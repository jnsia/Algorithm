#include <iostream>
using namespace std;

const int MAX = 1000001;

int N;
short primes[MAX];

int main()
{
	cin.tie(0);
	cout.tie(0);
	iostream::sync_with_stdio(false);

	for (int i = 2; i < MAX; i++)
	{
		if (primes[i] == 1) continue;

		for (int j = 2; j < 1001; j++)
		{
			if (i % j == 0) {
				for (int k = j + j; k < MAX; k += j)
				{
					primes[k] = 1;
				}
				break;
			}
		}
	}


	while (1) {
		cin >> N;

		if (N == 0) break;

		if (N % 2 == 1) {
			cout << "Goldbach's conjecture is wrong." << "\n";
			continue;
		}

		for (int i = 3; i < MAX / 2 + 1; i += 2)
		{
			if (primes[i] == 0 && primes[N - i] == 0) {
				cout << N << " = " << i << " + " << N - i << "\n";
				break;
			}
		}

		// cout << "Goldbach's conjecture is wrong." << "\n";
	}
}
