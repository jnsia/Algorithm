#include <iostream>
using namespace std;

int main(void) {
	int N;
	char str[101];
	char start, end;

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> str;

		start = str[0];

		for (int j = 0; j < 1001; j++)
		{
			if (str[j] == NULL) break;
			end = str[j];
		}

		cout << start << end << endl;
	}
}