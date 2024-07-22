#include <iostream>
#include<algorithm>
using namespace std;

const int MAX = 100001;

char number[MAX];

int main(void) {
	cin >> number;

	short is_exist_zero = 0;
	int sum_number = 0;
	int number_length = 0;

	for (int i = 0; i < MAX; i++)
	{
		if (number[i] == NULL) break;

		if (number[i] == '0') is_exist_zero = 1;

		sum_number += number[i] - '0';
		number_length = i + 1;
	}

	sort(number, number + number_length);

	if (is_exist_zero == 0 || sum_number % 3 != 0) {
		cout << "-1";
	}
	else {
		for (int i = 0; i < number_length; i++)
		{
			cout << number[number_length - i - 1];
		}
	}

    return 0;
}