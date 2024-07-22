#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> heights;

    // 입력 받기
    for (int i = 0; i < 9; ++i) {
        int height;
        cin >> height;
        heights.push_back(height);
    }

    int total = 0;
    for (int height : heights) {
        total += height;
    }

    int one = 0, two = 0;

    for (int i = 0; i < 9; ++i) {
        for (int j = i + 1; j < 9; ++j) {
            if (total - (heights[i] + heights[j]) == 100) {
                one = heights[i];
                two = heights[j];
                break;
            }
        }
    }

    heights.erase(find(heights.begin(), heights.end(), one));
    heights.erase(find(heights.begin(), heights.end(), two));

    sort(heights.begin(), heights.end());

    for (int height : heights) {
        cout << height << endl;
    }

    return 0;
}
