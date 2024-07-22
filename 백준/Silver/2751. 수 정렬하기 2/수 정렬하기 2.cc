#include <iostream>
using namespace std;

int arr[1000000];
int temp[1000000];

void merge(int arr[], int start, int end) {
    
    int mid = (start + end) / 2;
    
    int left = start;
    int right = mid + 1;
    int key = start;

    while (left <= mid && right <= end) {
        if (arr[left] < arr[right]) temp[key++] = arr[left++];
        else temp[key++] = arr[right++];
    }

    while (key <= end) {
        if (left <= mid) {
            temp[key++] = arr[left++];
        }
        else {
            temp[key++] = arr[right++];
        }
    }

    for (int i = start; i <= end; i++)
    {
        arr[i] = temp[i];
    }
}

void partition(int arr[], int start, int end) {
    if (start < end) {
        int mid = (start + end) / 2;
        partition(arr, start, mid);
        partition(arr, mid + 1, end);
        merge(arr, start, end);
    }
}


int main()
{
    ios::sync_with_stdio(0); // false
    cin.tie(0); // NULL
    cout.tie(NULL); // 0

    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    partition(arr, 0, N - 1);

    for (int i = 0; i < N; i++)
    {
        cout << arr[i] << "\n";
    }

    return 0;
}
