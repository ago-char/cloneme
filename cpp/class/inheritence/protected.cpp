// in protected inheritence, protected and public members of parent class will
// be accessibe as protected members of child class

#include <iostream>
using namespace std;

class parent {
   private:
    int privateMem;

   protected:
    int protectedMem;

   public:
    parent(int pri = 0, int pro = 0) {
        cout << "Construcotr in parent" << endl;
        privateMem = pri;
        protectedMem = pro;
    }
    void setData(int pri, int pro) {
        privateMem = pri;
        protectedMem = pro;
    }
    void printData() { cout << privateMem << " and " << protectedMem << endl; }
};

class child : protected parent {
   private:
    int x, y;

   public:
    child(int a, int b) : parent() {
        cout << "ChildConstructor\n";
        x = a;
        y = b;
    }
    void setParentData(int a, int b) { setData(a, b); }
    void displayData() { cout << x << " and " << y << endl; }
    void printParentData() { printData(); }
};

int main(void) {
    // i am comment
    child obj(1, 2);
    cout << "Child's Data : " << endl;
    obj.displayData();
    cout << "Parent's Data : " << endl;
    obj.printParentData();
    parent var(33, 43);
    cout << "Data from obj of parent : " << endl;
    var.printData();
    return 0;
}