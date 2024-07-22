#include <iostream>
using namespace std;

int main(void) {
	int N, M, i, j, temp;
	int arr[101];
	int temp_arr[101];
	
	cin >> N >> M;

	for (int i = 0; i < 101; i++)
	{
		arr[i] = i;
	}

	for (int line = 0; line < M; line++)
	{
		cin >> i >> j;

		for (int s = i; s <= j; s++)
		{
			temp_arr[s] = arr[s];
		}

		for (int s = i; s <= j; s++) {
			arr[s] = temp_arr[j - (s - i)];
		}
	}

	for (int idx = 1; idx <= N; idx++) cout << arr[idx] << " ";
}