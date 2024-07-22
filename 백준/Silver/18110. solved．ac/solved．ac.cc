#include <iostream>
using namespace std;

int N;
int arr[300001];
int temp[300001];

static void merge(int left, int right) {
	int mid = (left + right) / 2;

	int i = left;
	int j = mid + 1;
	int k = left;

	while (i <= mid && j <= right) {
		if (arr[i] > arr[j]) temp[k++] = arr[j++];
		else temp[k++] = arr[i++];
	}

	while (k <= right) {
		if (i <= mid) temp[k++] = arr[i++];
		else temp[k++] = arr[j++];
	}

	for (int i = left; i <= right; i++)
	{
		arr[i] = temp[i];
	}
}

static void partition(int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;

		partition(left, mid);
		partition(mid + 1, right);
		merge(left, right);
	}
}

static int fround(double num) {
	int res = (int) num;

	if (num >= res + 0.5) {
		res += 1;
	}

	return res;
}

int main()
{
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	int M = fround(N * 0.15);
	double answer = 0;

	partition(0, N - 1);

	for (int i = M; i < N - M; i++)
	{
		answer += arr[i];
	}

	if (N == 0) {
		cout << 0;
	}
	else {
		cout << fround(answer / (N - 2 * M));
	}
}

