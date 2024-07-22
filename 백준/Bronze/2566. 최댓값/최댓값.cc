#include <iostream>
using namespace std;

int matrix[9][9];

int main(void) {
	int max_row, max_col, temp;
	int max_value = -1;

	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++) {
			cin >> temp;

			if (temp > max_value) {
				max_row = i;
				max_col = j;
				max_value = temp;
			}
		}
	}

	cout << max_value << endl;
	cout << max_row + 1 << " " << max_col + 1;

	return 0;
}