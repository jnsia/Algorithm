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

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    int N, temp;
    cin >> N;

    Dequeue deque;
    Dequeue numbers;

    for (int i = 1; i < N + 1; i++)
    {
        cin >> temp;
        deque.addRear(temp);
        numbers.addRear(i);
    }

    int data, num;

    for (int i = 0; i < N; i++)
    {
        deque.deleteFront(data);
        numbers.deleteFront(num);

        cout << num << " ";

        if (data > 0) {
            for (int i = 0; i < data - 1; i++)
            {
                deque.deleteFront(temp);
                deque.addRear(temp);
                numbers.deleteFront(num);
                numbers.addRear(num);
            }
        }
        else {
            for (int i = data; i < 0; i++)
            {
                deque.deleteRear(temp);
                deque.addFront(temp);
                numbers.deleteRear(num);
                numbers.addFront(num);
            }
        }
    }

    return 0;
}
