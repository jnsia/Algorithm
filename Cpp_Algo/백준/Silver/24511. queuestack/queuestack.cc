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

    void deleteFront(int& data) {
        if (front == NULL) {
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
            data = temp->data;
            delete temp;
        }
    }

    void deleteRear(int& data) {
        if (rear == NULL) {
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
            data = temp->data;
            delete temp;
        }
    }
};

int N, M;
int A[100000], B[100000], C[100000];

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }

    for (int i = 0; i < N; i++)
    {
        cin >> B[i];
    }

    cin >> M;

    for (int i = 0; i < M; i++)
    {
        cin >> C[i];
    }

    Dequeue deque;

    for (int i = 0; i < N; i++)
    {
        if (A[i] == 0) deque.addFront(B[i]);
    }

    for (int i = 0; i < M; i++)
    {
        deque.addRear(C[i]);
    }

    int data;

    for (int i = 0; i < M; i++)
    {
        deque.deleteFront(data);
        cout << data << " ";
    }

    return 0;
}
