#include <iostream>
using namespace std;

#define min(x, y) ((x > y) ? (y) : (x))
#define max(x, y) ((x > y) ? (x) : (y))
#define abs(x) ((x > 0) ? (x) : (-x))

int cards[100];

int main(void) {
	int N , M;
	cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		cin >> cards[i];
	}

	int answer = 900001;

	for (int i = 0; i < N - 2; i++)
	{
		for (int j = i + 1; j < N - 1; j++)
		{
			int temp = 0;

			for (int k = j + 1; k < N; k++)
			{
				temp = cards[i] + cards[j] + cards[k];

				if (abs(answer - M) > abs(temp - M)) {
					answer = temp;
				}
			}
		}
	}

	cout << answer;

    return 0;
}