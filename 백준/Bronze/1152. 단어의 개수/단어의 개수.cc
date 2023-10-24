#include <iostream>
using namespace std;

int main(void) {
	char str[1000001];
	cin.getline(str, 1000001);

	int cnt = 0;
	short is_word = 0;

	for (int i = 0; i < 1000001; i++)
	{
		if (str[i] == NULL) break;

		if (str[i] == ' ') {
			if (is_word == 1) {
				cnt++;
				is_word = 0;
			}
		}
		else {
			is_word = 1;
		}
	}

	if (is_word) cnt++;

	cout << cnt;
}