#include <iostream>
using namespace std;

int main()
{
	int X, Y, N, a, b;
	cin >> X >> N;
	Y = 0;

	for (int i = 0; i < N; i++)
	{
		cin >> a >> b;
		Y += a * b;
	}

	if (X == Y) {
		cout << "Yes";
	}
	else {
		cout << "No";
	}
}
