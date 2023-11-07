#include <iostream>
using namespace std;

#define max(x, y) ((x > y) ? (x) : (y))

int main() {
	int N;
	cin >> N;

	int answer = -1;

	for (int i = 0; i <= N / 3; i++)
	{
		int temp = N;

		temp -= 5 * i;

		if (temp < 0) {
			break;
		}

		if (temp % 3 == 0) {
			answer = i + temp / 3;
		}
	}

	cout << answer;

	return 0;
}