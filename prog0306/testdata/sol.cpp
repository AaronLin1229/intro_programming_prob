#include <bits/stdc++.h>
using namespace std;

string grade_to_letter(int grade) {
    if (grade >= 90) return "A+";
    else if (grade >= 85) return "A";
    else if (grade >= 80) return "A-";
    else if (grade >= 77) return "B+";
    else if (grade >= 73) return "B";
    else if (grade >= 70) return "B-";
    else if (grade >= 67) return "C+";
    else if (grade >= 63) return "C";
    else if (grade >= 60) return "C-";
    else return "F";
}

int main() {
    int grade;
    cin >> grade;
    cout << grade_to_letter(grade);
    return 0;
}
