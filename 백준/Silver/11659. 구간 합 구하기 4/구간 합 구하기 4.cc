#include <iostream>
using namespace std;

int numbers[100000];

int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	int N, M;
	cin >> N >> M;

	for (int i = 1; i < N + 1; i++)
	{
		cin >> numbers[i];
	}

	for (int i = 1; i < N + 1; i++)
	{
		numbers[i] += numbers[i - 1];
	}

	int i, j;

	for (int k = 0; k < M; k++)
	{
		cin >> i >> j;

		cout << numbers[j] - numbers[i - 1] << "\n";
	}

	return 0;
}