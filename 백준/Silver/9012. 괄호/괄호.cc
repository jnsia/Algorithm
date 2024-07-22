#include <iostream>
using namespace std;

char str[51];
char stack[51];

void clearStack() {
	for (int i = 0; i < 51; i++)
	{
		stack[i] = NULL;
	}
}

int main(void) {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		clearStack();
		cin >> str;

		short is_correct = true;
		int size = 0;

		for (int i = 0; i < 51; i++)
		{
			if (str[i] == NULL) break;

			if (str[i] == '(') {
				stack[size++] = '(';
			}
			else {
				if (stack[size - 1] == '(') {
					size--;
				}
				else {
					is_correct = false;
					break;
				}
			}
		}

		if (is_correct && size == 0) {
			cout << "YES" << "\n";
		}
		else {
			cout << "NO" << "\n";
		}
	}

	return 0;
}