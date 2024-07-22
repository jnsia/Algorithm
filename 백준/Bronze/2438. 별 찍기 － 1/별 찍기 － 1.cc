#include <iostream>
using namespace std;

int main()
{
	int T;

	cin >> T;

	for (int i = 1; i < T + 1; i++)
	{
		for (int j = 0; j < i; j++)
		{
			cout << "*";
		}

		cout << endl;
	}
}
