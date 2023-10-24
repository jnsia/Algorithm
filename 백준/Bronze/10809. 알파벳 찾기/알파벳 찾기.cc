#include <iostream>
using namespace std;

int main(void) {
	char str[101];
	int str_idx[26], temp;
	cin >> str;

	for (int i = 0; i < 26; i++)
	{
		str_idx[i] = -1;
	}

	for (int i = 0; i < 101; i++)
	{
		if (str[i] == NULL) break;

		temp = int(str[i]) - int('a');
		
		if (str_idx[temp] == -1) str_idx[temp] = i;
	}

	for (int i = 0; i < 26; i++)
	{
		cout << str_idx[i] << " ";
	}
}