#include <iostream>
#include <algorithm>
using namespace std;

#define max(a, b) ((a > b) ? (a) : (b))

class Node {
public:
    int leftIndex;
    int rightIndex;
    long long int value;

    Node() {
        this->leftIndex = -1;
        this->rightIndex = -1;
        this->value = 0;
    }

    Node(int leftIndex, int rightIndex, long long int value) {
        this->leftIndex = leftIndex;
        this->rightIndex = rightIndex;
        this->value = value;
    }
};

int N, temp, length;
long long int arr[1001];
Node leftArray[1000001];
Node rightArray[1000001];

static bool compare(int v1, int v2) {
    return v1 < v2;
}

static bool compare2(Node v1, Node v2) {
    return v1.value < v2.value;
}

static long long int binarySearch(long long int key, long long int end) {
    long long int low = 0;
    long long int high = end - 1;

    while (low <= high) {
        long long int mid = (low + high) / 2;

        if (rightArray[mid].value == key) {
            return arr[rightArray[mid].rightIndex];
        }
        else if (rightArray[mid].value > key) {
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }
    }

    return -1;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    sort(arr, arr + N, compare);

    int leftSize = 0;
    int rightSize = 0;

    for (int i = 0; i < N; i++)
    {
        for (int j = i; j < N; j++) {
            leftArray[leftSize++] = Node(i, j, arr[i] + arr[j]);
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++) {
             rightArray[rightSize++] = Node(i, j, arr[j] - arr[i]);
        }
    }

    sort(rightArray, rightArray + rightSize, compare2);

    long long int answer = 0;

    for (int i = 0; i < leftSize; i++)
    {
        long long int result = binarySearch(leftArray[i].value, rightSize);

        if (result != -1) answer = max(answer, result);
    }

    cout << answer;

    return 0;
}
