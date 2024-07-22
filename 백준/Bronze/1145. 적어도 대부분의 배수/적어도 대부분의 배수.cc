#include <iostream>
using namespace std;

int arr[5];

int main()
{
	for (int i = 0; i < 5; i++)
	{
		cin >> arr[i];
	}

	int num = 1;

	while (true)
	{
		int res = 0;

		for (int i = 0; i < 5; i++)
		{
			if (num % arr[i] == 0) {
				res++;
			}
		}

		if (res >= 3) break;

		num++;
	}

	cout << num;
}

