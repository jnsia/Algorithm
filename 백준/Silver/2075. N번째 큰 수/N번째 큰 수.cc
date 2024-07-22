#include <iostream>
using namespace std;

const int MIN = -1000000001;

int N;
int board[1500][1500];
int rows[1500];
int datas[1500];

int main(void) {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		rows[i] = N - 1;

		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
		}
	}

	int size = 0;

	while (size < N) {
		int max_v = MIN;
		int max_i = -1;

		for (int i = 0; i < N; i++)
		{
			int v = board[rows[i]][i];

			if (v > max_v) {
				max_v = v;
				max_i = i;
			}
		}

		datas[size++] = max_v;
		rows[max_i]--;
	}

	int answer = datas[0];

	for (int i = 1; i < size; i++)
	{
		if (datas[i] < answer) {
			answer = datas[i];
		}
	}

	cout << answer;

    return 0;
}