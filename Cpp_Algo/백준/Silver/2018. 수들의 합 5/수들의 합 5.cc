#include <iostream>
using namespace std;

int main(void) {
	int N;
	cin >> N;

	int left = 0;
	int right = 0;
	int sum = 0;
	int answer = 0;

	while (left <= right && right <= N) {
		if (sum == N) {
			right++;
			sum += right;
			answer++;
		}
		else if (sum > N) {
			left++;
			sum -= left;
		}
		else {
			right++;
			sum += right;
		}
	}

	cout << answer;

	return 0;
}
