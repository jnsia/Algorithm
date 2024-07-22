#include <iostream>
using namespace std;

int main(void) {
	int T, R;
	char str[21];
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		cin >> R >> str;
		
		for (int k = 0; k < 21; k++)
		{
			if (str[k] == NULL) break;
			
			for (int j = 0; j < R; j++)
			{
				cout << str[k];
			}
		}

		cout << endl;
	}
}