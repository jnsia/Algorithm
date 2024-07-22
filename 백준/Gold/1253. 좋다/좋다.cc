#include <iostream>
using namespace std;

// 배열 초기화
int N;
long long int arr[2000];
long long int temp[2000];

short is_good(int now) {
	int result = 0;

	int left = 0;
	int right = N - 1;
	int key = arr[now];

	while (left < right) {
		if (left == now) {
			left++;
			continue;
		}
		else if (right == now) {
			right--;
			continue;
		}

		int sum = arr[left] + arr[right];
		// cout << sum << " " << key << endl;

		if (sum == key) {
			result++;
			break;
		}
		else if (sum > key) {
			right--;
		}
		else {
			left++;
		}
	}
	
	return result;
}

// 병합
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

// 분할
void partition(int l, int r) {
	if (l < r) {
		int mid = (l + r) / 2;
		partition(l, mid);
		partition(mid + 1, r);
		merge(l, r);
	}
}

int main(void) {
	// 입력
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	// merge sort
	partition(0, N - 1);

	int answer = 0;

	for (int i = 0; i < N; i++)
	{
		if (is_good(i) == 1) {
			answer++;
		}
	}

	cout << answer;

	return 0;
}
