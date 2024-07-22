#include <iostream>
using namespace std;

int main(void) {
	char str[101];
	int char_len = 0;

	cin >> str;

	for (int i = 0; i < 100; i++)
	{
		if (str[i] == NULL) break;
		
		char_len += 1;
	}

	int cnt = char_len;

	for (int i = 0; i < char_len; i++) {
		if (str[i] == '=') {
			if (str[i - 1] == 'c') cnt--;
			if (str[i - 1] == 's') cnt--;
			if (str[i - 1] == 'z') {
				cnt--;
				if (str[i - 2] == 'd') cnt--;
			}
		}

		if (str[i] == '-') {
			if (str[i - 1] == 'c') cnt--;
			if (str[i - 1] == 'd') cnt--;
		}

		if (str[i] == 'j') {
			if (str[i - 1] == 'l') cnt--;
			if (str[i - 1] == 'n') cnt--;
		}
	}
	cout << cnt;

	return 0;
}