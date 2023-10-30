#include <iostream>
using namespace std;

char matrix[101][101];

int main(void) {
	int N, x, y;
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> x >> y;

		for (int j = 0; j < 10; j++)
		{
			for (int k = 0; k < 10; k++)
			{
				matrix[x + j][y + k] = 1;
			}
		}
	}

	int area = 0;

	for (int i = 0; i < 101; i++)
	{
		for (int j = 0; j < 101; j++)
		{
			if (matrix[i][j] == 1) {
				area += 1;
			}
		}
	}

	cout << area;

	return 0;
}