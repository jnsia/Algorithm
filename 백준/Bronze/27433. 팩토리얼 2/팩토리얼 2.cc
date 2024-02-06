#include <iostream>
using namespace std;

long long int recursion(long long int num) {
	if (num == 0 || num == 1) return 1;
	return recursion(num - 1) * num;
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
