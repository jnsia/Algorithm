#include <iostream>
using namespace std;

char str[101];
char stack[101];

struct Node {
	int data;
	Node* next;
};

void clearStack() {
	for (int i = 0; i < 51; i++)
	{
		stack[i] = NULL;
	}
}

int main(void) {
	while (1)
	{
		clearStack();
		cin.getline(str, 101, '\n');

		if (str[0] == '.') break;

		short is_correct = true;
		int size = 0;

		for (int i = 0; i < 101; i++)
		{
			if (str[i] == '.') break;

			if (str[i] == '(') {
				stack[size++] = '(';
			}
			else if (str[i] == '[') {
				stack[size++] = '[';
			}
			else if (str[i] == ')') {
				if (stack[size - 1] == '(') {
					size--;
				}
				else {
					is_correct = false;
					break;
				}
			}
			else if (str[i] == ']') {
				if (stack[size - 1] == '[') { 
					size--; 
				}
				else {
					is_correct = false;
					break;
				}
			}
			else {
				continue;
			}
  		}

		if (is_correct && size == 0) {
			cout << "yes" << "\n";
		}
		else {
			cout << "no" << "\n";
		}
	}

	return 0;
}