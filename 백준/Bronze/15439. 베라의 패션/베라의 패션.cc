#include <iostream>
using namespace std;

long long int N;

int main(void) {

	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

	cin >> N;

	cout << N * (N - 1);

    return 0;
}