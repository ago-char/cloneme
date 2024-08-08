// 1. struct keyword while accessing struct data type created with the help of
// struct is optional, wheread in C it was compulsary
#include <string.h>

#include <iostream>
using namespace std;
int main(void) {
    // let's create a struct named student
    struct student {
       private:
        int age, grade;
        char name[20], address[34];

       public:
        void setData(int a, int g, char* naam, char* place) {
            age = a;
            grade = g;
            strcpy(name, naam);
            strcpy(address, place);
        }
        void showData() {
            cout << "Name : " << name << endl;
            cout << "Address : " << address << endl;
            cout << "Grade : " << grade << endl;
            cout << "Age : " << age << endl;
        }
    };

    // with use of struct keyword
    struct student s1;
    // without use of struct keyword
    student s2;
    // set data of both students
    s1.setData(18, 12, (char*)"Smarika Nepal", (char*)"Sukrabare");
    s2.setData(19, 12, (char*)"Deeya Pokheral", (char*)"Ramailo");
    // display info of both students
    s1.showData();
    cout << ".........................." << endl;
    s2.showData();

    return 0;
}