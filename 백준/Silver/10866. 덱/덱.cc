#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* prev;
    Node* next;

    Node(int data) {
        this->data = data;
        this->prev = NULL;
        this->next = NULL;
    }
};

class Deque {
public:
    int size;
    Node* front;
    Node* rear;

    Deque() {
        size = 0;
        front = NULL;
        rear = NULL;
    }

    void push_front(int data) {
        Node* node = new Node(data);

        if (size == 0) {
            front = node;
            rear = node;
        }
        else {
            front->prev = node;
            node->next = front;
            front = node;
        }

        size++;
    }

    void push_back(int data) {
        Node* node = new Node(data);

        if (size == 0) {
            front = node;
            rear = node;
        }
        else {
            rear->next = node;
            node->prev = rear;
            rear = node;
        }

        size++;
    }

    void pop_front() {
        if (size == 0) {
            cout << -1 << "\n";
            return;
        }

        Node* node = front;
        size--;

        if (size == 0) {
            front = NULL;
            rear = NULL;
        }
        else {
            front = front->next;
        }

        cout << node->data << "\n";
        node = NULL;
    }

    void pop_back() {
        if (size == 0) {
            cout << -1 << "\n";
            return;
        }

        Node* node = rear;
        size--;

        if (size == 0) {
            front = NULL;
            rear = NULL;
        }
        else {
            rear = rear->prev;
        }

        cout << node->data << "\n";
        node = NULL;
    }

    void check_size() {
        cout << size << "\n";
    }

    void empty() {
        if (size == 0) cout << 1 << "\n";
        else cout << 0 << "\n";
    }

    void check_front() {
        if (size == 0) cout << -1 << "\n";
        else cout << front->data << "\n";
    }

    void check_back() {
        if (size == 0) cout << -1 << "\n";
        else cout << rear->data << "\n";
    }
};

char cmd[11];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    int N, X;
    cin >> N;

    Deque deque = Deque();

    for (int i = 0; i < N; i++)
    {
        cin >> cmd;

        if (cmd[0] == 'p') {
            if (cmd[1] == 'u') {
                cin >> X;

                if (cmd[5] == 'f') {
                    deque.push_front(X);
                }
                else {
                    deque.push_back(X);
                }
            }
            else {
                if (cmd[4] == 'f') {
                    deque.pop_front();
                }
                else {
                    deque.pop_back();
                }
            }
        }
        else if (cmd[0] == 's') {
            deque.check_size();
        }
        else if (cmd[0] == 'e') {
            deque.empty();
        }
        else if (cmd[0] == 'f')
        {
            deque.check_front();
        }
        else {
            deque.check_back();
        }
    }

    return 0;
}
