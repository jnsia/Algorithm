#include <iostream>
using namespace std;

char matrix[16][16];

int main(void) {
	for (int i = 0; i < 16; i++)
	{
		if (cin.eof()) break;
		
		cin >> matrix[i];
	}

	for (int i = 0; i < 15; i++)
	{
		for (int j = 0; j < 15; j++)
		{
			if (matrix[j][i] == NULL) continue;

			cout << matrix[j][i];
		}
	}

	return 0;
}