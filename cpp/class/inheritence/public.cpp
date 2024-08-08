#include <iostream>
using namespace std;

class A {
   private:
    int privateVar;

   protected:
    int protectedVar;

   public:
    A(int priv = 1, int prot = 0) {
        cout << "Hello Constructor of A" << endl;
        privateVar = priv;
        protectedVar = prot;
    }
    void getData() {
        cout << "Private = " << privateVar << endl;
        cout << "Protected = " << protectedVar << endl;
    }
    void nothing() { cout << "Nothing Just Like this\n"; }
};

class B : public A {
   public:
    B() { cout << "Hello B ko Constructor\n"; }
};

// Driver Code
int main(void) {
    B obj;
    obj.nothing();
    obj.getData();
    return 0;
}