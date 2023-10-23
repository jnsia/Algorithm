#include <iostream>
using namespace std;

int main()
{
	short is_true;
	int year;

	is_true = 0;
	cin >> year;

	if (year % 4 == 0) {
		if (!(year % 100 == 0) || (year % 400 == 0)) {
			is_true = 1;
		}
	}

	if (is_true) {
		cout << 1;
	}
	else {
		cout << 0;
	}
}