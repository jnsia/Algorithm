#include <iostream>
using namespace std;

int main(void) {
	int temp;
	short num[43];

	for (int i = 0; i < 43; i++)
	{
		num[i] = 0;
	}

	for (int i = 0; i < 10; i++) {
		cin >> temp;
		temp %= 42;
		num[temp] = 1;
	}

	int cnt = 0;

	for (int i = 0; i < 43; i++)
	{
		if (num[i] == 1) cnt++;
	}

	cout << cnt;
}