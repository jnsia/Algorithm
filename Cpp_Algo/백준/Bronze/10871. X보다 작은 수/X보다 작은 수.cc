#include <iostream>
using namespace std;

int main(void) {
	int N, X;
	int arr[10001];

	cin >> N >> X;
	
	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	for (int i = 0; i < N; i++)
	{
		if (arr[i] < X) {
			cout << arr[i] << " ";
		}
	}
}