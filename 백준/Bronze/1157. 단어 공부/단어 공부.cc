#include <iostream>
using namespace std;

int main(void) {
	char str[1000001];
	int alphabet[26], max_cnt, max_idx;
	short is_dup = 0;
	cin >> str;

	for (int i = 0; i < 26; i++)
	{
		alphabet[i] = 0;
	}

	for (int i = 0; i < 1000001; i++)
	{
		if (str[i] == NULL) break;

		if (int(str[i]) >= int('a')) {
			alphabet[int(str[i]) - int('a')] += 1;
		}
		else {
			alphabet[int(str[i]) - int('A')] += 1;
		}
	}

	max_cnt = 0;
	max_idx = -1;

	for (int i = 0; i < 26; i++)
	{
		if (alphabet[i] > max_cnt) {
			max_cnt = alphabet[i] ;
			max_idx = i;
			is_dup = 0;
		}
		else if (alphabet[i] == max_cnt) {
			is_dup = 1;
		}
	}

	if (is_dup) cout << '?';
	else cout << char(max_idx + int('A'));
}