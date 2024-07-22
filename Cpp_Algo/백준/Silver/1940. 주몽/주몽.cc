#include <iostream>
using namespace std;

int arr[15000];
int temp[15000];

void merge(int l, int r) {
	int mid = (l + r) / 2;

	int i = l;
	int j = mid + 1;
	int k = l;

	while (i <= mid && j <= r) {
		if (arr[i] > arr[j]) {
			temp[k++] = arr[j++];
		}
		else {
			temp[k++] = arr[i++];
		}
	}

	while (k <= r) {
		if (i > mid) {
			temp[k++] = arr[j++];
		}
		else {
			temp[k++] = arr[i++];
		}
	}

	for (int s = l; s <= r; s++)
	{
		arr[s] = temp[s];
	}
}

void partition(int l, int r) {
	if (l < r) {
		int mid = (l + r) / 2;
		partition(l, mid);
		partition(mid + 1, r);
		merge(l, r);
	}
}

int main(void) {
	int N, M;
	cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	partition(0, N - 1);

	int left = 0;
	int right = N - 1;
	int answer = 0;

	while (left < right) {
		int sum = arr[left] + arr[right];

		if (sum == M) {
			right--;
			left++;
			answer++;
		}
		else if (sum > M) {
			right--;
		}
		else {
			left++;
		}
	}

	cout << answer;

	return 0;
}
