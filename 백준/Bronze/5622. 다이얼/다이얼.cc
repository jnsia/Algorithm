#include <iostream>
using namespace std;

int main(void) {
	char str[16];
	cin >> str;

	int time = 0;

	for (int i = 0; i < 16; i++)
	{
		if (str[i] == NULL) break;

		if (int(str[i]) >= int('W')) time += 10;
		else if (int(str[i]) >= int('T')) time += 9;
		else if (int(str[i]) >= int('P')) time += 8;
		else if (int(str[i]) >= int('M')) time += 7;
		else if (int(str[i]) >= int('J')) time += 6;
		else if (int(str[i]) >= int('G')) time += 5;
		else if (int(str[i]) >= int('D')) time += 4;
		else if (int(str[i]) >= int('A')) time += 3;
	}

	cout << time;
}