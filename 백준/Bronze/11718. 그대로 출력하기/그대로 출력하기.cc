#include <iostream>
using namespace std;

int main(void) {
	char str[101];
	
	while (1) {
		if (cin.eof()) break;

		cin.getline(str, 101);

		for (int i = 0; i < 101; i++)
		{
			if (str[i] == NULL) break;
			cout << str[i];
		}

		cout << endl;
	}
}