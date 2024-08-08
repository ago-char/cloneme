// they are called instance members because they are only created when you
// create or define or declare object or instance of class, if you do not create
// no memory will be allocated to instance members
#include <iostream>
using namespace std;
class square {
    // no need to declare as private as they are by default
    // following are instance member variables
    int length;
    // but need to declare pub func
    // following are instance member functions/methods
   public:
    void setLen(int l) { length = l; }
    int getLen() { return length; }
    int getArea() { return length * length; }
    int getPerm() { return 4 * length; }
};

int main(void) {
    // instances or objects of class 'square'
    square s1, s2;
    // if you call getArea without calling setLen you will get garbage which
    // compiler set
    cout << s1.getArea() << endl;
    // so first vall setlen
    s1.setLen(5);
    // not get area and perm
    cout << s1.getArea() << endl;
    cout << s1.getPerm() << endl;

    return 0;
}