#include <iostream>

using namespace std;

class Singleton {
public:
    static Singleton& GetInstance() {
        // Allocate with `new` in case Singleton is not trivially destructible.
        static Singleton* singleton = new Singleton();
        return *singleton;
    }

private:
    Singleton() = default;

    // Delete copy/move so extra instances can't be created/moved.
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;
    Singleton(Singleton&&) = delete;
    Singleton& operator=(Singleton&&) = delete;
};

int main() {
    Singleton *st,*st2;
    
    cout << "Singleton Class instance created !" << endl;
    cout <<st->GetInstance << endl;
    cout << st2->GetInstance<< endl;
    return 0;
}