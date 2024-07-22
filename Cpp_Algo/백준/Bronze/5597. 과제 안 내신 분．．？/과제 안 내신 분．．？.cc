#include <iostream>
using namespace std;

int main(void) {
	int temp;
	short num[31];

	for (int i = 0; i < 31; i++)
	{
		num[i] = 0;
	}

	for (int i = 0; i < 28; i++) {
		cin >> temp;
		num[temp] = 1;
	}

	for (int i = 1; i < 31; i++)
	{
		if (num[i] == 0) cout << i << endl;
	}
}