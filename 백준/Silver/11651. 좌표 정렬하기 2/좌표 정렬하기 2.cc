#include <iostream>
using namespace std;

struct coord {
    int x;
    int y;
};

// left가 더 큼 = 0
// right가 더 큼 = 1
short compareCoord(coord left, coord right) {
    if (left.y > right.y) {
        return 1;
    }
    else if (left.y == right.y && left.x > right.x) {
        return 1;
    }

    return 0;
}

void merge(coord coords[], coord temp[], int left, int right) {
    if (left > right) return;

    int mid = (left + right) / 2;
    int i = left;
    int j = mid + 1;
    int k = left;

    while (i <= mid && j <= right) {
        if (compareCoord(coords[i], coords[j]) == 0) temp[k++] = coords[i++];
        else temp[k++] = coords[j++];
    }

    while (k <= right) {
        if (i <= mid) temp[k++] = coords[i++];
        else temp[k++] = coords[j++];
    }

    for (int idx = left; idx <= right; idx++)
    {
        coords[idx] = temp[idx];
    }
}

void partition(coord coords[], coord temp[], int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;
        partition(coords, temp, left, mid);
        partition(coords, temp, mid + 1, right);
        merge(coords, temp, left, right);
    }
}

int N, xi, yi;
coord coords[100000];
coord temp[100000];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> coords[i].x >> coords[i].y;
    }

    partition(coords, temp, 0, N - 1);

    for (int i = 0; i < N; i++)
    {
        cout << coords[i].x << " " << coords[i].y << "\n";
    }

    return 0;
}
