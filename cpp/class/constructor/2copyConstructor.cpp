#include <iostream>
using namespace std;

class bike {
    int gear, max_speed;
    bool isDiskBrake;
    int diskBrake_N;

   public:
    // even if you do not create any constructor, compiler will create one, if
    // you create one default constructor compiler will not create any but it
    // will still create copy constructor

    bike(int GEAR = 5, int MAX_SPEED = 200, bool DISBRAKE_Y_N = false,
         int DISBRAKE_TOTAL = 0) {
        gear = GEAR;
        max_speed = MAX_SPEED;
        isDiskBrake = DISBRAKE_Y_N;
        if (isDiskBrake)
            diskBrake_N = DISBRAKE_TOTAL;
        else
            diskBrake_N = 0;
    }

    // if you do not create any copy constructor compiler will create one but if
    // you create copy constructor compiler will not create any (not even
    // default constructor so make sure you make one default too because you
    // won't be able to create any obj if you do not define any default
    // constructor ). you need to pass reference of obj (mind you not the obj
    // itself, it will run into infinite loop)
    bike(bike &b) {
        gear = 23;
        max_speed = 480390;
        isDiskBrake = false;
        diskBrake_N = 2;
    }
    void details() {
        cout << "Gear = " << gear << " MaximumSpeed = " << max_speed << endl;
        if (isDiskBrake) {
            cout << "Diskbrake is Present and Number of Disk Brake in the bike "
                    "= "
                 << diskBrake_N << endl;
        } else
            cout << "DiskBrake Not Available for this bike.\n";
    }
};
int main(void) {
    // i am comment
    bike b1;                   // default conf
    bike b2(4, 160, true, 1);  // not default
    bike b3(6, 400, true, 3);

    b1.details();
    // copy to b1, the details of b2
    // b1 = b2;
    // new variable using copy constructor
    bike b4(b1);
    b4.details();
    b1.details();
    return 0;
}