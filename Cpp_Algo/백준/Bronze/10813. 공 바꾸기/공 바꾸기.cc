#include <iostream>
using namespace std;

int main(void) {
	int N, M, i, j, temp;
	int arr[101];
	
	cin >> N >> M;

	for (int i = 0; i < 101; i++)
	{
		arr[i] = i;
	}

	for (int line = 0; line < M; line++)
	{
		cin >> i >> j;

		temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	for (int idx = 1; idx <= N; idx++) cout << arr[idx] << " ";
}