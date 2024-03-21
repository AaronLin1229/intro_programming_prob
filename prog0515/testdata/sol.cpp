#include <bits/stdc++.h>
using namespace std;

vector<int> mergeArrays(vector<int>& A, vector<int>& B) {
    vector<int> C;
    int i = 0, j = 0;
    while (i < A.size() && j < B.size()) {
        if (A[i] < B[j]) {
            C.push_back(A[i++]);
        } else {
            C.push_back(B[j++]);
        }
    }
    while (i < A.size()) {
        C.push_back(A[i++]);
    }
    while (j < B.size()) {
        C.push_back(B[j++]);
    }
    return C;
}

int main() {
    int N, M, num;
    cin >> N;
    vector<int> A, B;
    for (int i = 0; i < N; ++i) {
        cin >> num;
        A.push_back(num);
    }
    cin >> M;
    for (int i = 0; i < M; ++i) {
        cin >> num;
        B.push_back(num);
    }
    vector<int> C = mergeArrays(A, B);
    for (int num : C) {
        cout << num << " ";
    }
    return 0;
}
