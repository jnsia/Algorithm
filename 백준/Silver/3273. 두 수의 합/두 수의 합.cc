#include <iostream>
using namespace std;

int arr[100001];
int temp[100001];

void merge(int left, int right, int arr[], int temp[]) {
    int mid = (left + right) / 2;

    int i = left;
    int j = mid + 1;
    int k = left;

    while (i <= mid && j <= right) {
        if (arr[i] > arr[j]) {
            temp[k++] = arr[j++];
        }
        else {
            temp[k++] = arr[i++];
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
}

void partition(int left, int right, int arr[], int temp[]) {
    if (left < right) {
        int mid = (left + right) / 2;
        partition(left, mid, arr, temp);
        partition(mid + 1, right, arr, temp);
        merge(left, right, arr, temp);
    }
}


int main()
{
    int N, X;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    partition(0, N - 1, arr, temp);

    cin >> X;

    int answer = 0;
    int j = N - 1;

    for (int i = 0; i < N - 1; i++)
    {
        while (i < j) {
            int temp = arr[i] + arr[j];
 
            if (temp == X) {
                answer++;
            }
            else if (temp < X) {
                break;
            }

            j--;
        }
    }

    cout << answer;

    return 0;
}
