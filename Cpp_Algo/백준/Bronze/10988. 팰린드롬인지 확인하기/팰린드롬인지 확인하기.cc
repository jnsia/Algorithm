#include <iostream>
using namespace std;

int main(void) {
	char str[101];
	cin >> str;
	int len;
	short is_pal = true;

	for (int i = 0; i < 101; i++)
	{
		len = i;
		if (str[i] == NULL) break;
	}

	for (int i = 0; i < len / 2; i++)
	{
		if (str[i] != str[len - 1 - i]) {
			is_pal = false;
			break;
		}
	}

	if (is_pal) cout << 1;
	else cout << 0;
}