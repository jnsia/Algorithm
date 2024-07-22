#include <iostream>
using namespace std;

int gcd(int a, int b) {
	int c;

	while (b > 0) {
		c = a % b;
		a = b;
		b = c;
	}
	
	return a;
}

int N, M, gcd_num;

int main(void) {

	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

	cin >> N >> M;

	gcd_num = gcd(N, M);
	cout << gcd(N, M) << "\n";
	cout << (N * M) / gcd_num;

    return 0;
}