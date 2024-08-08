// you do not have any concept of data security in C, where as you can use
// constructor or any input function to secure data inside struct
#include <stdlib.h>
#include <string.h>

#include <iostream>
using namespace std;

int main(void) {
    struct road {
       private:
        char name[20];  // road name for GOOGLE
        float length;   // in Kms
       public:
        // use of constructor and initiate variable as no name and length as
        // 0KM, which will help in checking condition
        road() {
            name[0] = '\0';
            length = 0;
        }
        void setName(char* naam) {
            if (naam) strcpy(name, naam);
        }
        void setLen(float len) {
            if (len < 0) length = -len;
            length = len;
            if (!len) {
                cout << "You can not set Length to 0 as it is by default set. "
                        "Give Valid Length of Road.\n";
            }
        }
        float getLen() {
            if (length > 0) return length;
            cout << "Length is not set Yet. Please use setLen() utility. "
                    "Default Vale is 0KM.\n";
            return 0.0F;
        }
        char* getName() {
            int l = strlen(name);
            char* road_name = (char*)malloc(l + 1);
            if (l > 0) {
                strcpy(road_name, name);
                road_name[l] = '\0';
                return road_name;
            }
            cout << "Name is not set yet. Please use setName() utility\n";
            road_name = NULL;
            return road_name;
        }
    };
    // Main Code Here
    road r1, r2;
    r2.setLen(0.0F);
    r1.setLen(4.6L);
    int l;
    if ((l = r1.getLen()) > 0)
        cout << "Road 1 Length  = " << l << " KM." << endl;
    r2.setName((char*)"H01");
    cout << "Road 2 name is = " << r2.getName() << endl;
    return 0;
}