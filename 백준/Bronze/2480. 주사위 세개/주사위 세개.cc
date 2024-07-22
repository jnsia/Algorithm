#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int a, b, c;
	cin >> a >> b >> c;

	if (a == b && b == c) {
		cout << 1000 * a + 10000;
	}
	else if (a == b) {
		cout << 100 * a + 1000;
	}
	else if (b == c) {
		cout << 100 * b + 1000;
	}
	else if (a == c) {
		cout << 100 * c + 1000;
	}
	else {
		cout << 100 * max({a, b, c});
	}
}
