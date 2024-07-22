#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* prev;
    Node* next;
};

class Dequeue {
private:
    int size;
    Node* front;
    Node* rear;

public:
    Dequeue() {
        size = 0;
        front = NULL;
        rear = NULL;
    }

    ~Dequeue() {
        
    }

    void addFront(int data) {
        Node* newNode;
        newNode = new Node;
        newNode->data = data;
        newNode->prev = NULL;

        if (rear == NULL) {
            rear = newNode;
            newNode->next = NULL;
        }
        else {
            newNode->next = front;
            front->prev = newNode;
        }
        
        size++;
        front = newNode;
    }

    void addRear(int data) {
        Node* newNode;
        newNode = new Node;
        newNode->data = data;
        newNode->next = NULL;

        if (front == NULL) {
            front = newNode;
            newNode->prev = NULL;
        }
        else {
            newNode->prev = rear;
            rear->next = newNode;
        }

        size++;
        rear = newNode;
    }

    void deleteFront() {
        if (front == NULL) {
            cout << -1 << "\n";
        }
        else {
            Node* temp;
            temp = front;
            front = front->next;

            if (front == NULL) {
                rear = NULL;
            }
            else {
                front->prev = NULL;
            }

            size--;
            cout << temp->data << "\n";
            delete temp;
        }
    }

    void deleteRear() {
        if (rear == NULL) {
            cout << -1 << "\n";
        }
        else {
            Node* temp;
            temp = rear;
            rear = rear->prev;

            if (rear == NULL) {
                front = NULL;
            }
            else {
                rear->next = NULL;
            }


            size--;
            cout << temp->data << "\n";
            delete temp;
        }
    }

    void getFront() const {
        if (front == NULL) {
            cout << -1 << "\n";
        }
        else {
            cout << front->data << "\n";
        }
    }

    void getRear() const {
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
};

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    int N, cmd, data;
    cin >> N;

    Dequeue deque;

    for (int i = 0; i < N; i++)
    {
        cin >> cmd;

        if (cmd == 1) { 
            cin >> data;
            deque.addFront(data);
        }
        else if (cmd == 2) {
            cin >> data;
            deque.addRear(data);
        }
        else if (cmd == 3) deque.deleteFront();
        else if (cmd == 4) deque.deleteRear();
        else if (cmd == 5) deque.length();
        else if (cmd == 6) deque.empty();
        else if (cmd == 7) deque.getFront();
        else if (cmd == 8) deque.getRear();
    }

    return 0;
}
