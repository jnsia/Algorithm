#include <iostream>
#include <algorithm>
using namespace std;

int T, N, M;
int memo1[1000001];
int memo2[1000001];

int binary_search(int size, int key) {
	int low = 0;
	int high = size - 1;

	while (low <= high)
	{
		int mid = (low + high) / 2;

		if (memo1[mid] == key) {
			return 1;
		}
		else if (memo1[mid] > key) {
			high = mid - 1;
		}
		else {
			low = mid + 1;
		}
	}

	return 0;
}

int main(void) {
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

	cin >> T;

	for (int i = 0; i < T; i++)
	{
		cin >> N;

		for (int j = 0; j < N; j++)
		{
			cin >> memo1[j];
		}

		sort(memo1, memo1 + N);

		cin >> M;

		for (int j = 0; j < M; j++)
		{
			cin >> memo2[j];
		}

		for (int j = 0; j < M; j++)
		{
			cout << binary_search(N, memo2[j]) << "\n";
		}
	}

    return 0;
}