#include <iostream>
using namespace std;

int N, M;
int arr[1000001];
int parent[1000001];
int result[1000001];
char tmp[1001];

int find_set(int x) {
    if (parent[x] == x) {
        return parent[x];
    }

    parent[x] = find_set(parent[x]);
    return parent[x];
}

void union_set(int x, int y) {
    x = find_set(x);
    y = find_set(y);

    if (x > y) parent[x] = y;
    else parent[y] = x;
}

void dfs(int idx) {
    if (find_set(idx) != find_set(idx + arr[idx])) {
        union_set(idx, idx + arr[idx]);
        dfs(idx + arr[idx]);
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    cin >> N >> M;

    int cnt = 0;

    for (int i = 0; i < N; i++)
    {
        cin >> tmp;

        for (int j = 0; j < M; j++)
        {
            if (tmp[j] == 'U') arr[cnt] = -M;
            if (tmp[j] == 'D') arr[cnt] = M;
            if (tmp[j] == 'L') arr[cnt] = -1;
            if (tmp[j] == 'R') arr[cnt] = 1;

            parent[cnt] = cnt;
            cnt++;
        }
    }

    for (int i = 0; i < cnt; i++)
    {
        dfs(i);
    }

    for (int i = 0; i < cnt; i++)
    {
        result[parent[i]] = 1;
    }

    int answer = 0;

    for (int i = 0; i < cnt; i++)
    {
        if (result[i] == 1) answer++;
    }

    cout << answer;

    return 0;
}
