#include <iostream>
using namespace std;

void merge(int arr[], int tmp[], int left, int right) {
	int mid = (left + right) / 2;

	int i = left;
	int j = mid + 1;
	int k = left;

	while (i <= mid && j <= right) {
		if (arr[i] > arr[j]) tmp[k++] = arr[j++];
		else tmp[k++] = arr[i++];
	}

	while (k <= right) {
		if (i <= mid) tmp[k++] = arr[i++];
		else tmp[k++] = arr[j++];
	}

	for (int idx = left; idx <= right; idx++)
	{
		arr[idx] = tmp[idx];
	}
}

void partition(int arr[], int tmp[], int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;

		partition(arr, tmp, left, mid);
		partition(arr, tmp, mid + 1, right);
		merge(arr, tmp, left, right);
	}
}

int binary_search(int arr[], int key, int low, int high) {
	while (low <= high) {
		int mid = (low + high) / 2;

		if (arr[mid] == key) {
			return 1;
		} else if (arr[mid] > key) {
			high = mid - 1;
		}
		else {
			low = mid + 1;
		}
	}

	return 0;
}

int N, M, key;
int arr[100000];
int tmp[100000];

int main(void) {

	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

    cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	partition(arr, tmp, 0, N - 1);

	cin >> M;

	for (int i = 0; i < M; i++)
	{
		cin >> key;
		cout << binary_search(arr, key, 0, N - 1) << "\n";
	}

    return 0;
}