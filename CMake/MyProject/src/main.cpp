#include<bits/stdc++.h>
using namespace std;

class Entity {
private:
    int e_id;
    string e_name;

public:
    explicit Entity(int id, string name) {
        e_id = id;
        e_name = name;
    }

    Entity() = delete;
    Entity(int id) = delete;
    Entity(string name) = delete;

    int getID() {
        return e_id;
    }
    string getName() {
        return e_name;
    }
};

void print(Entity e) {
    cout<<e.getID()<<" "<<e.getName()<<endl;
}

int main() {
    // solution
    Entity a(1, "Drake");
    Entity b(2, "Snoop Dogg");

    print(a);
    print(b);
    return 0;
}