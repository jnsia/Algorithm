#include <iostream>
using namespace std;

int main(void) {
	char str[101];
	int len;

	cin >> str;

	for (int i = 0; i < 101; i++)
	{
		len = i;
		if (str[i] == NULL) break;
	}

	cout << len;
}