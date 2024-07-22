#include <iostream>
using namespace std;

int main(void) {
	int N, M, i, j, k;
	int arr[101];
	
	cin >> N >> M;

	for (int i = 0; i < 101; i++)
	{
		arr[i] = 0;
	}

	for (int line = 0; line < M; line++)
	{
		cin >> i >> j >> k;

		for (int idx = i; idx <= j; idx++) {
			arr[idx] = k;
		}
	}

	for (int idx = 1; idx <= N; idx++) cout << arr[idx] << " ";
}