#include <iostream>
using namespace std;

class Node {
public:
    long long int key;
    long long int value;

    Node() {
        this->key = 0;
        this->value = 0;
    }

    Node(long long int key, long long int value) {
        this->key = key;
        this->value = value;
    }
};

long long int N, P, Q;
Node nodes[1000001];

int nodes_length = 0;

static long long int is_exist(long long int key) {
    long long int result = 0;

    for (int i = 0; i < nodes_length; i++)
    {
        if (nodes[i].key == key) {
            result = nodes[i].value;
            break;
        }
    }

    return result;
}

static long long int devide_conquer(long long int key) {
    long long int result = is_exist(key);

    if (key == 0) return 1;

    if (result == 0) {
        long long int value = devide_conquer(key / P) + devide_conquer(key / Q);
        nodes[nodes_length++] = Node(key, value);
        return value;
    }
    else {
        return result;
    }
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    cin >> N >> P >> Q;

    long long int answer = devide_conquer(N);

    cout << answer;

    return 0;
}
