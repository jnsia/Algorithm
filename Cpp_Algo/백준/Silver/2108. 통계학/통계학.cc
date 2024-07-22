#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

#define max(x, y) ((x > y) ? (x) : (y))
#define min(x, y) ((x < y) ? (x) : (y))

int arr[500001];
int counting[8001];
int stack[8001];

int main()
{
	int N;
	cin >> N;

	double sum = 0;
	int min_v = 4001;
	int max_v = -4001;

	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
		sum += arr[i];
		counting[arr[i] + 4000] += 1;
		min_v = min(min_v, arr[i]);
		max_v = max(max_v, arr[i]);
	}

	int preq_cnt = -1;
	int preq_num;

	int size = 0;

	for (int i = 0; i < 8001; i++)
	{
		if (counting[i] > preq_cnt) {
			size = 0;
			stack[size++] = i - 4000;
			preq_cnt = counting[i];
		}
		else if (counting[i] == preq_cnt) {
			stack[size++] = i - 4000;
		}
	}
	
	if (size >= 2) {
		preq_num = stack[1];
	}
	else {
		preq_num = stack[0];
	}

	sort(arr, arr + N);

	printf("%1.f\n", round(sum / N) + 0);
	printf("%d\n", arr[N / 2]);
	printf("%d\n", preq_num);
	printf("%d\n", max_v - min_v);
}

