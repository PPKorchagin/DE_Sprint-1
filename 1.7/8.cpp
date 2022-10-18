#include <iostream>
#include <string>
#include <time.h>
using namespace std;


int arr[5][5] = {};

void aprint() {
    int i;
    int j;
    cout << "\t";
    for (i=0;i<5;i++) {
        cout << "[" << i << "]\t";
    }
    cout << endl;

    for (i=0;i<5;i++) {
        cout << "[" << i << "]\t";
        for (j=0;j<5;j++) {
            cout << arr[i][j] << "\t";
        }
        cout << endl;
    }
}

int amax() {
    int max=0;

    int i;
    int j;
    for (i=0;i<5;i++) {
        for (j=0;j<5;j++) {
            if (arr[i][j]>max) {
                max=arr[i][j];
            }
        }
    }

    return max;
}

int amin() {
    int min=61;

    int i;
    int j;
    for (i=0;i<5;i++) {
        for (j=0;j<5;j++) {
            if (arr[i][j]<min) {
                min=arr[i][j];
            }
        }
    }

    return min;
}

int main() {
    srand(time(NULL));

    int i;
    int j;

    for (i=0;i<5;i++) {
        for (j=0;j<5;j++) {
            arr[i][j]=30+rand()%30;
        }
    }


    cout << "Forst elem is " << arr[0][0] << endl;

    cout << "Max element is " << amax() << endl;
    cout << "Min element is " << amin() << endl;

}