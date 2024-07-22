#include <iostream>
using namespace std;

int N, C;
int left_things[15];
int right_things[15];
long long int left_sum[32768];
long long int right_sum[32768];
long long int temp[32768];
int left_size;
int right_size;

int upper_bound(long long int key) {
	int low = 0;
	int high = right_size - 1;
	
	while (low <= high) {
		int mid = (low + high) / 2;
		long long int sum = right_sum[mid] + key;

		if (sum <= C) {
			low = mid + 1;
		}
		else {
			high = mid - 1;
		}
	}
	
	return high;
}

void merge(int left, int right) {
	int mid = (left + right) / 2;

	int i = left;
	int j = mid + 1;
	int k = left;

	while (i <= mid && j <= right) {
		if (right_sum[i] > right_sum[j]) {
			temp[k++] = right_sum[j++];
		}
		else {
			temp[k++] = right_sum[i++];
		}
	}

	while (k <= right) {
		if (i > mid) {
			temp[k++] = right_sum[j++];
		}
		else {
			temp[k++] = right_sum[i++];
		}
	}

	for (int idx = left; idx <= right; idx++)
	{
		right_sum[idx] = temp[idx];
	}
}

void partition(int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		partition(left, mid);
		partition(mid + 1, right);
		merge(left, right);
	}
}

int left_comb(int idx, long long int res, int end) {
	if (idx == end) {
		left_sum[left_size++] = res;
		return 0;
	}

	left_comb(idx + 1, res, end);
	left_comb(idx + 1, res + left_things[idx], end);
	
	return 0;
}

int right_comb(int idx, long long int res, int end) {
	if (idx == end) {
		right_sum[right_size++] = res;
		return 0;
	}

	right_comb(idx + 1, res, end);
	right_comb(idx + 1, res + right_things[idx], end);

	return 0;
}

int main(void) {
	cin >> N >> C;

	int mid = N / 2;

	for (int i = 0; i < mid; i++)
	{
		cin >> left_things[i];
	}

	for (int i = 0; i < N - mid; i++)
	{
		cin >> right_things[i];
	}

	left_size = 0;
	right_size = 0;

	left_comb(0, 0, mid);
	right_comb(0, 0, N - mid);

	partition(0, right_size - 1);

	int answer = 0;

	for (int i = 0; i < left_size; i++)
	{
		int result = upper_bound(left_sum[i]);
		answer += result + 1;
	}

	cout << answer;

    return 0;
}