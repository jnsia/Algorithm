#include <iostream>
using namespace std;

int N;
long long int fact[13];

int main(void) {

	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

	cin >> N;

	fact[0] = 1;
	fact[1] = 1;

	for (int i = 2; i < 13; i++)
	{
		fact[i] = fact[i - 1] * i;
;	}

	cout << fact[N];

    return 0;
}