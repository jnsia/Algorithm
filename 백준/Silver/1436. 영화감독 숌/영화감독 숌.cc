#include <iostream>
using namespace std;

#define max(x, y) ((x > y) ? (x) : (y))

short check_666(int number) {
	int result = 0;
	int temp;

	while (number > 0) {
		temp = number % 10;

		if (temp == 6) {
			result += 1;
		}
		else {
			result = 0;
		}

		if (result == 3) {
			return 1;
		}

		number = number / 10;
	}

	return 0;
}

int main() {
	int N;
	cin >> N;

	int cur_num = 666;
	int cnt = 0;

	while (1) {
		if (check_666(cur_num) == 1) {
			cnt += 1;
		}

		if (cnt == N) {
			break;
		}

		cur_num += 1;
	}

	cout << cur_num;

	return 0;
}