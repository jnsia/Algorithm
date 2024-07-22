#include <iostream>
using namespace std;

int main(void) {
	int N, sum_value;
	char str[101];
	cin >> N >> str;

	sum_value = 0;

	for (int i = 0; i < N; i++)
	{
		sum_value += int(str[i]) - int('0');
	}

	cout << sum_value;
}