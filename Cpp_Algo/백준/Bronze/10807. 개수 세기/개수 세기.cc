#include <iostream>
using namespace std;

int main(void) {
	int N, v;
	int arr[101];

	cin >> N;
	
	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	cin >> v;

	int cnt = 0;

	for (int i = 0; i < N; i++)
	{
		if (arr[i] == v) {
			cnt++;
		}
	}

	cout << cnt;
}