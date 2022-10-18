#include <iostream>
#include <string>
#include <time.h>
#include <algorithm>
using namespace std;


struct student {
    string surname;
    string initials;
    int group_number;
    int rate[5];
};

float get_middle(int arr[5]) {
    int sum=0;
    int i;
    for (i=0;i<5;i++){
        sum+=arr[i];
    }
    return float(sum)/5;
}



int main() {
    student students[10];

    student stud1={"Bolton","R",4,{1,4,2,1,4},};
    students[0]=stud1;

    student stud2={"Snow","D",1,{5,4,5,5,4},};
    students[1]=stud2;

    student stud3={"Stark","A",3,{5,5,5,5,5},};
    students[2]=stud3;

    student stud4={"Lanister","T",4,{4,4,4,4,5},};
    students[3]=stud4;

    student stud5={"Lanister","D",1,{2,2,1,3,2},};
    students[4]=stud5;

    student stud6={"Grayjoy","T",2,{5,3,2,1,5},};
    students[5]=stud6;

    student stud7={"Barateon","S",2,{3,4,5,5,1},};
    students[6]=stud7;

    student stud8={"Aaron","D",1,{2,4,5,5,4},};
    students[7]=stud8;

    student stud9={"Targarien","D",5,{5,5,5,5,3},};
    students[8]=stud9;

    student stud10={"Mormount","D",3,{4,4,4,5,5},};
    students[9]=stud10;

    student sorted[10];

    int i;

    int middles[10]={};

    cout << "Orig:" << endl;
    for (i=0;i<10;i++) {
        float middle=get_middle(students[i].rate);
        cout << "#" << i << " " << students[i].surname << ": " << middle << endl;
        middles[i]=i;
    }

    cout << "\nSorted:" << endl;

    int j;
    int l;
    for (l=0;l<8;l++) {
        for (j=0;j<9;j++) {
            if (get_middle(students[middles[j]].rate)>get_middle(students[middles[j+1]].rate)) {
                int temp_st_index=middles[j+1];
                middles[j+1]=middles[j];
                middles[j]=temp_st_index;
            }
        }
    }

    int k;
    for (k=0;k<10;k++) {
        float middle=get_middle(students[middles[k]].rate);
        cout << "#" << middles[k] << " " << students[middles[k]].surname << ": " << middle << endl;
        sorted[k]=students[middles[k]];
    }

    cout << "\nFiltered:" << endl;
    for (k=0;k<10;k++) {
        bool only45=true;
        for (l=0;l<5;l++) {
            if (sorted[k].rate[l]<4) {
                only45=false;
                break;
            }
        }
        if (only45) {
            float middle=get_middle(sorted[k].rate);
            cout << "#" << middles[k] << " " << sorted[k].surname << ": " << middle << endl;
        }
    }
}