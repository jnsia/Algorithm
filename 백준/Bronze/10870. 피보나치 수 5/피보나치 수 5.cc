#include <iostream>
using namespace std;

int recursion(int num) {
	if (num == 0) return 0;
	if (num == 1) return 1;
	if (num == 2) return 1;
	return recursion(num - 1) + recursion(num - 2);
}

int main()
{
	cin.tie(0);
	cout.tie(0);
	iostream::sync_with_stdio(false);

	int N;
	cin >> N;

	cout << recursion(N);
}
