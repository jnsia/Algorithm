#include <iostream>
using namespace std;

struct node {
    int idx;
    int data;
};

// left가 더 큼 = 0
// right가 더 큼 = 1
short compareCoord(node left, node right) {
    if (left.data > right.data) {
        return 1;
    }
    else {
        return 0;
    }
}

void merge(node nodes[], node temp[], int left, int right) {
    if (left > right) return;

    int mid = (left + right) / 2;
    int i = left;
    int j = mid + 1;
    int k = left;

    while (i <= mid && j <= right) {
        if (compareCoord(nodes[i], nodes[j]) == 0) temp[k++] = nodes[i++];
        else temp[k++] = nodes[j++];
    }

    while (k <= right) {
        if (i <= mid) temp[k++] = nodes[i++];
        else temp[k++] = nodes[j++];
    }

    for (int idx = left; idx <= right; idx++)
    {
        nodes[idx] = temp[idx];
    }
}

void partition(node nodes[], node temp[], int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;
        partition(nodes, temp, left, mid);
        partition(nodes, temp, mid + 1, right);
        merge(nodes, temp, left, right);
    }
}

int N;
node nodes[1000000];
node temp[1000000];
int answer[1000000];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        nodes[i].idx = i;
        cin >> nodes[i].data;
    }

    partition(nodes, temp, 0, N - 1);

    int prev_data = -1000000001;
    int rank = 0;

    for (int i = 0; i < N; i++)
    {
        if (nodes[i].data > prev_data) {
            answer[nodes[i].idx] = rank++;
        }
        else {
            answer[nodes[i].idx] = rank - 1;
        }

        prev_data = nodes[i].data;
    }

    for (int i = 0; i < N; i++)
    {
        cout << answer[i] << " ";
    }

    return 0;
}
