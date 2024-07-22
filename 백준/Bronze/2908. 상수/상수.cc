#include <iostream>
using namespace std;

int main(void) {
	int A, B, rA, rB;
	cin >> A >> B;

	rA = 0;
	rB = 0;

	while (A > 0) {
		rA *= 10;
		rA += A % 10;
		A /= 10;
	}

	while (B > 0) {
		rB *= 10;
		rB += B % 10;
		B /= 10;
	}

	if (rA > rB) {
		cout << rA;
	}
	else {
		cout << rB;
	}
}