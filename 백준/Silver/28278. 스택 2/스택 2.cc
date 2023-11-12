#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* prev;
};

class Stack {
private:
    int size;
    Node* top;

public:
    Stack() {
        size = 0;
        top = NULL;
    }
    
    ~Stack() {

    }

    bool isEmpty() const {
        if (top == NULL) {
            cout << 1 << "\n";
            return true;
        }
        else {
            cout << 0 << "\n";
            return false;
        }
    }
    
    void push(int data) {
        Node* newNode;
        newNode = new Node;
        newNode->data = data;
        if (top == NULL) {
            newNode->prev = NULL;
            top = newNode;
        }
        else {
            newNode->prev = top;
            top = newNode;
        }
        size++;
    }

    void pop() {
        if (top == NULL) {
            cout << -1 << "\n";
        }
        else {
            Node* temp;
            temp = top;
            top = top->prev;
            cout << temp->data << "\n";
            delete temp;
            size--;
        }
    }

    void length() const {
        cout << size << "\n";
    }

    void peek() const {
        if (top == NULL) {
            cout << -1 << "\n";
        }
        else {
            cout << top->data << "\n";
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

    Stack stack;
    int cmd, data;

    for (int i = 0; i < N; i++)
    {
        cin >> cmd;

        if (cmd == 1) {
            cin >> data;
            stack.push(data);
        }
        else if (cmd == 2) {
            stack.pop();
        }
        else if (cmd == 3) {
            stack.length();
        }
        else if (cmd == 4) {
            stack.isEmpty();
        }
        else {
            stack.peek();
        }
    }

    return 0;
}
