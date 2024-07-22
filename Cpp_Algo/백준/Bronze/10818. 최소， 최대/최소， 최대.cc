#include <iostream>
using namespace std;

int main(void) {
	int N, max_value, min_value, temp;

	cin >> N;

	max_value = -1000001;
	min_value = 1000001;
	
	for (int i = 0; i < N; i++)
	{
		cin >> temp;

		if (temp > max_value) {
			max_value = temp;
		}

		if (temp < min_value) min_value = temp;
	}

	cout << min_value << " " << max_value;
}