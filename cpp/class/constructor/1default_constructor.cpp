#include <iostream>
using namespace std;

class bike {
    int gear, max_speed;
    bool isDiskBrake;
    int diskBrake_N;

   public:
    /*   constructor is member function which is public(because you want
       constructor to be called ), it the the function which will have as
       same name as class and has no return type
       */
    // even if you do not create one constructor, compiler will create
    bike() {}
    // but if you wanna initialise some value at the time of obj creation, you
    // can overload it and we will talk in next session
};
int main(void) {
    // i am comment

    return 0;
}