#include <iostream>
using namespace std;

int N, K, Y, M;

int main(void) {
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

	cin >> N;

	Y = 0;
	M = 0;

	for (int i = 0; i < N; i++)
	{
		cin >> K;

		Y += (K / 30 + 1) * 10;
		M += (K / 60 + 1) * 15;
	}

	if (Y == M) cout << "Y M " << Y;
	else if (Y > M) cout << "M " << M;
	else cout << "Y " << Y;

    return 0;
}