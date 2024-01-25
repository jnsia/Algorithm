#include <iostream>
using namespace std;

#define min(x, y) (((x) < (y)) ? (x) : (y));
#define abs(x) ((x > 0) ? (x) : (-x));

int N, X, Y;
int arr[101];
int graph[101][101];
int comb1[101];
int comb2[101];
int answer = 100001;
int queue[10001];
int visited[101];

static short check(int comb[]) {
    int num = 0;
    int start = 0;

    for (int i = 1; i < N + 1; i++)
    {
        if (comb[i] == 1) { 
            num++;
            visited[i] = 0;

            if (start == 0) start = i;
        }
        else {
            visited[i] = 1;
        }

    }
    
    if (num == 0 || num == N) return 0;

    int front = 0;
    int rear = 0;
    int res = 1;

    queue[rear++] = start;
    visited[start] = 1;

    while (front < rear) {
        int now = queue[front++];

        for (int i = 1; i < N + 1; i++)
        {
            if (graph[now][i] == 1 && visited[i] == 0) {
                visited[i] = 1;
                res++;
                queue[rear++] = i;
            }
        }
    }

    if (num == res) return 1;
    else return 0;
}

static void comb(int idx) {
    if (idx == N + 1) {
        for (int i = 1; i < N + 1; i++)
        {
            if (comb1[i] == 0) {
                comb2[i] = 1;
            }
            else {
                comb2[i] = 0;
            }

        }


        if (check(comb1) == 1 && check(comb2) == 1) {
            int sum1 = 0;
            int sum2 = 0;

            for (int i = 1; i < N + 1; i++)
            {
                if (comb1[i] == 1) sum1 += arr[i];
                if (comb2[i] == 1) sum2 += arr[i];
            }

            int diff = abs((sum1 - sum2));
            answer = min(answer, diff);

        }
        
        return;
    }

    comb1[idx] = 1;
    comb(idx + 1);
    comb1[idx] = 0;
    comb(idx + 1);

    return;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    cin >> N;
    
    for (int i = 1; i < N + 1; i++)
    {
        cin >> arr[i];
    }

    for (int i = 1; i < N + 1; i++)
    {
        cin >> X;

        for (int j = 0; j < X; j++)
        {
            cin >> Y;
            graph[i][Y] = 1;
            graph[Y][i] = 1;
        }
    }

    comb(1);

    if (answer == 100001) {
        cout << -1;
    }
    else {
        cout << answer;
    }

    return 0;
}
