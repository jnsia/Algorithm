#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

class Queue {
private:
    int size;
    Node* front;
    Node* rear;

public:
    Queue() {
        size = 0;
        front = NULL;
        rear = NULL;
    }

    ~Queue() {
        
    }

    void front_peek() const {
        if (front == NULL) {
            cout << -1 << "\n";
        }
        else {
            cout << front->data << "\n";
        }
    }

    void back_peek() const {
        if (rear == NULL) {
            cout << -1 << "\n";
        }
        else {
            cout << rear->data << "\n";
        }
    }

    void length() {
        cout << size << "\n";
    }

    void empty() const {
        if (front == NULL) {
            cout << 1 << "\n";
        }
        else {
            cout << 0 << "\n";
        }
    }

    void push(int data) {
        Node* newNode;
        newNode = new Node;
        newNode->data = data;
        newNode->next = NULL;

        if (front == NULL) {
            front = newNode;
        }
        else {
            rear->next = newNode;
        }
        
        rear = newNode;
        size++;
    }

    void pop() {
        if (front == NULL) {
            cout << -1 << "\n";
        }
        else {
            Node* temp;
            temp = new Node;
            temp = front;
            front = front->next;
            
            if (front == NULL) {
                rear = NULL;
            }

            size--;
            cout << temp->data << "\n";
            delete temp;
        }
    }
};

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    int N;
    cin >> N;

    Queue queue;
    string cmd;
    int data;

    for (int i = 0; i < N; i++)
    {
        cin >> cmd;

        if (cmd == "front") {
            queue.front_peek();
        }
        else if (cmd == "back") {
            queue.back_peek();
        }
        else if (cmd == "size") {
            queue.length();
        }
        else if (cmd == "empty") {
            queue.empty();
        }
        else if (cmd == "pop") {
            queue.pop();
        }
        else {
            cin >> data;
            queue.push(data);
        }
    }

    return 0;
}
