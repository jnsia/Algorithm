#include <iostream>
using namespace std;

int arr[1000];
int temp[1000];

int merge(int left, int right) {
	int mid = (left + right) / 2;

	int i = left;
	int j = mid + 1;
	int k = left;

	while (i <= mid && j <= right) {
		if (arr[i] <= arr[j]) {
			temp[k++] = arr[i++];
		}
		else {
			temp[k++] = arr[j++];
		}
	}

	while (k <= right) {
		if (i > mid) {
			temp[k++] = arr[j++];
		}
		else {
			temp[k++] = arr[i++];
		}
	}

	for (int i = left; i <= right; i++)
	{
		arr[i] = temp[i];
	}

	return 0;
}

void partition(int left, int right) {
	int mid;

	if (left < right) {
		mid = (left + right) / 2;

		partition(left, mid);
		partition(mid + 1, right);
		merge(left, right);
	}
}

int main() {
	int N;
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	partition(0, N - 1);

	for (int i = 0; i < N; i++)
	{
		cout << arr[i] << endl;
	}

	return 0;
}