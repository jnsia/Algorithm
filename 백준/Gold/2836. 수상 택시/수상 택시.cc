#include <iostream>
using namespace std;

int N, M;

class Node {
public:
    long long int start;
    long long int end;

    Node(int start, int end) {
        this->start = start;
        this->end = end;
    }
};

Node* arr[300000];
Node* tmp[300000];

short compare(Node* node1, Node* node2) {
    if (node1->start < node2->start) return 1;
    else if (node1->start > node2->start) return -1;
    else {
        if (node1->end < node2->end) return 1;
        else return -1;
    }
}

void merge(int left, int right) {
    int mid = (left + right) / 2;

    int i = left;
    int j = mid + 1;
    int k = left;

    while (i <= mid && j <= right) {
        if (compare(arr[i], arr[j]) == 1) tmp[k++] = arr[j++];
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

void partition(int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;

        partition(left, mid);
        partition(mid + 1, right);
        merge(left, right);
    }
}

int main() {
    cin >> N >> M;

    int size = 0;
    int start, end;

    for (int i = 0; i < N; i++)
    {
        cin >> start >> end;


        if (start > end) {
            Node* node = new Node(start, end);
            arr[size++] = node;
        }
    }

    partition(0, size - 1);

    long long int answer = M;
    
    Node* now = new Node(M + 1, M + 1);

    for (int i = 0; i < size; i++) {
        if (now->end > arr[i]->start) {
            answer += (now->start - now->end) * 2;
            now = arr[i];
        }
        else {
            if (now->end > arr[i]->end) {
                now->end = arr[i]->end;
            }
        }
    }

    answer += (now->start - now->end) * 2;

    cout << answer;

    return 0;
}