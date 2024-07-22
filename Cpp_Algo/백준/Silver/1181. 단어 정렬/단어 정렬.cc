#include <iostream>
using namespace std;

struct node {
    int length;
    char word[51];
};

// left가 더 큼 = 0
// right가 더 큼 = 1
short compareCoord(node left, node right) {
    if (left.length > right.length) {
        return 1;
    }
    else if (left.length == right.length) {
        int idx = 0;

        while (left.word[idx] == right.word[idx]) idx++;

        if (left.word[idx] > right.word[idx]) {
            return 1;
        }
    }
    
    return 0;
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
node nodes[20001];
node temp[20001];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    cin >> N;

    int size;

    for (int i = 0; i < N; i++)
    {
        cin >> nodes[i].word;
        
        size = 0;
        
        for (int j = 0; j < 51; j++)
        {
            size = j;
            if (nodes[i].word[j] == NULL) break;
        }

        nodes[i].length = size;
    }

    partition(nodes, temp, 0, N - 1);

    int rank = 0;

    for (int i = 0; i < N; i++)
    {
        short flag = 1;

        for (int j = 0; j < nodes[i].length; j++)
        {
            if (nodes[i].length != nodes[i + 1].length) {
                flag = 0;
                break;
            }

            if (nodes[i].word[j] != nodes[i + 1].word[j]) {
                flag = 0;
                break;
            }
        }

        if (flag == 0) {
            cout << nodes[i].word << "\n";
        }
    }

    return 0;
}
