#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int constructor = 0;

	for (int i = 1; i < N; i++)
	{
		int j = i;
		int temp = j;

		while (j > 0) {
			temp += j % 10;
			j /= 10;
		}

		if (temp == N) {
			constructor = i;
			break;
		}
	}

	cout << constructor;

	return 0;
}