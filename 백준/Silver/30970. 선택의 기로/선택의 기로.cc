#include <iostream>
using namespace std;

class Node {
public:
	int quality;
	int price;

	Node(int Q, int P) {
		this->quality = Q;
		this->price = P;
	}

	~Node() {};
};

int N, Q, P;
Node* arr[100001];
Node* temp[100001];

int compare1(Node* node1, Node* node2) {
	if (node1->quality > node2->quality) {
		return -1;
	}
	else if (node1->quality < node2->quality) {
		return 1;
	}
	else {
		if (node1->price > node2->price) {
			return 1;
		}
		else {
			return -1;
		}
	}
}

int compare2(Node* node1, Node* node2) {
	if (node1->price > node2->price) {
		return 1;
	}
	else if (node1->price < node2->price) {
		return -1;
	}
	else {
		if (node1->quality > node2->quality) {
			return -1;
		}
		else {
			return 1;
		}
	}
}

void merge(int left, int right, int type) {
	int mid = (left + right) / 2;

	int i = left;
	int j = mid + 1;
	int k = left;
	
	while (i <= mid && j <= right) {
		if (type == 1) {
			if (compare1(arr[i], arr[j]) == 1) temp[k++] = arr[j++];
			else temp[k++] = arr[i++];
		}
		else {
			if (compare2(arr[i], arr[j]) == 1) temp[k++] = arr[j++];
			else temp[k++] = arr[i++];
		}
	}

	while (k <= right) {
		if (i <= mid) temp[k++] = arr[i++];
		else temp[k++] = arr[j++];
	}

	for (int idx = left; idx <= right; idx++)
	{
		arr[idx] = temp[idx];
	}
};

void partition(int left, int right, int type) {
	if (left < right) {
		int mid = (left + right) / 2;
		partition(left, mid, type);
		partition(mid + 1, right, type);
		merge(left, right, type);
	}
}

int main(void) {
	cin >> N;
	
	for (int i = 0; i < N; i++)
	{
		cin >> Q >> P;

		Node* node = new Node(Q, P);
		arr[i] = node;
	}

	partition(0, N - 1, 1);
	
	cout << arr[0]->quality << " " << arr[0]->price << " " << arr[1]->quality << " " << arr[1]->price << "\n";

	partition(0, N - 1, 2);

	cout << arr[0]->quality << " " << arr[0]->price << " " << arr[1]->quality << " " << arr[1]->price << "\n";

    return 0;
}