#include <iostream>
using namespace std;

int main(void) {
	int a, b;
	cout.precision(10);

	cin >> a >> b;

	cout << a + b << endl;
	cout << a - b << endl;
	cout << a * b << endl;
	cout << a / b << endl;
	cout << a % b << endl;

	return 0;
}