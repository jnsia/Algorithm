#include <iostream>

using namespace std;

int arr[26];
char words[101][101];

int reset() {
	for (int i = 0; i < 26; i++)
	{
		arr[i] = 0;
	}

	return 0;
}

int main(void) {
	// 입력
	int N;
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> words[i];
	}

	// 로직
	int cnt = 0;
	int word_int;

	for (int i = 0; i < N; i++)
	{
		int temp = -1;

		for (int j = 0; j < 101; j++)
		{
			if (words[i][j] == NULL) {
				cnt += 1;
				break;
			}
			
			word_int = int(words[i][j]) - int('a');

			if (word_int != temp) {
				if (arr[word_int] == 0) {
					arr[word_int] = 1;
					temp = word_int;
				}
				else {
					break;
				}

			}

		}

		

		reset();
	}

	cout << cnt;

	return 0;
}