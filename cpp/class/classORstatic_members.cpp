// Features of class members variables are in seq 1,2,3,.... and Features of
// class member functions are in seq i,ii,iii,.........
#include <string.h>

#include <iostream>
using namespace std;

class person {
    int age;
    float height;
    char name[20];
    // 1. static mem var is declared inside class qualified with static keyword
    // and also known as class variable as it exists even if class object is not
    // made
    static char location[20];

   public:
    //    i.) static function can only access static member var.  Well non
    //    static can access both bust they requires object to be invoked, but
    //    static function can be invoked with or without object, so there is no
    //    such restriction that class variable must be set with member function,
    //    hence staic function is only option left
    // ii.) you may or may not specify definition outside class, if you declare
    // inside you must define outside otherwise no
    static void setLocation(char* place) {
        if (place) {
            strcpy(location, place);
        }
    }
    void setInfo(int AGE, float HEIGHT, char* NAME) {
        if (AGE < 0)
            age = -AGE;
        else
            age = AGE;
        if (HEIGHT < 0.0)
            height = -HEIGHT;
        else
            height = HEIGHT;
        if (name)
            strcpy(name, NAME);
        else
            name[0] = '\0';
    }
    person getInfo() {
        person p;
        p.age = age;
        p.height = height;
        strcpy(p.name, name);
        strcpy(p.location, location);
        return p;
    }
    int getAge() { return age; }
    float getHeight() { return height; }
    char* getLocation() {
        int len = strlen(location);
        if (len > 0) {
            char* loc = (char*)malloc(len + 1);
            strcpy(loc, location);
            loc[len] = '\0';
            return loc;
        }
        return NULL;
    }
};

// 2.static class member variable must be defined outside class and this does
// not belong to any specific object but to all object or whole class.
// 3. There will be only copy of static mem var for all obj and all will use the
// same copy, whereas this can be access even without object
char person::location[20] =
    "Gothgaun";  // you may want to initialize it(which is optional anyway ),
                 // default location as 'gothgaun'

int main(void) {
    // I am comment
    // 4. the only way to set location is to call setlocation function with or
    // without obj, this is with obj, later without obj iii.) class function can
    person p;
    cout << "Default : " << p.getLocation() << endl;
    p.setLocation((char*)"Biratnagar");
    cout << "After Change in state with obj : " << p.getLocation() << endl;
    // be called without object as such
    person::setLocation((char*)"SAlakpur");
    // but non static func can not be called without obj, they need obj
    // person::setInfo(1, 2.5F, (char*)"sagar");
    cout << "Change in state without obj : " << p.getLocation() << endl;

    return 0;
}