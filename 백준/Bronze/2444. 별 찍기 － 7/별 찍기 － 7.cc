#include <iostream>
using namespace std;

int main(void) {
	int N;
	cin >> N;

	for (int i = 1; i < N * 2; i++)
	{
		for (int j = 0; j < N * 2 - abs(N - i) - 1; j++)
		{
			if (abs(N - i) - j > 0) cout << " ";
			else cout << "*";
		}

		cout << endl;
	}
}