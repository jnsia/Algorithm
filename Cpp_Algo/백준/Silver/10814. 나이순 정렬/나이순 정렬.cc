#include <iostream>
using namespace std;

struct user {
    int age;
    char name[101];
};

// left가 더 큼 = 0
// right가 더 큼 = 1
short compareCoord(user left, user right) {
    if (left.age > right.age) {
        return 1;
    }
    else {
        return 0;
    }
}

void merge(user coords[], user temp[], int left, int right) {
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

void partition(user coords[], user temp[], int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;
        partition(coords, temp, left, mid);
        partition(coords, temp, mid + 1, right);
        merge(coords, temp, left, right);
    }
}

int N, xi, yi;
user users[100000];
user temp[100000];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> users[i].age >> users[i].name;
    }

    partition(users, temp, 0, N - 1);

    for (int i = 0; i < N; i++)
    {
        cout << users[i].age << " " << users[i].name << "\n";
    }

    return 0;
}
