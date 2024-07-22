#include <iostream>
using namespace std;

int main(void) {
	int max_value, max_idx, temp;

	max_value = -1;
	max_idx = 0;
	
	for (int i = 1; i < 10; i++)
	{
		cin >> temp;

		if (temp > max_value) {
			max_value = temp;
			max_idx = i;
		}
	}

	cout << max_value << endl << max_idx;
}