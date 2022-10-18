#include <iostream>
#include <string>
using namespace std;

int main() {

    float t;
    for (t=-4;t<=4;t+=0.5) {
        cout << t << ": " << -2*t*t-5*t - 8 << endl;
    }

    return 0;
}