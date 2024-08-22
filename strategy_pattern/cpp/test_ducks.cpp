#include "ducks.h"
#include <iostream>

using namespace std;

int main() {
    Duck mullard = MullardDuck();
    Duck red_head = RedHeadDuck();
    Duck decoy = Decoy();
    Duck rubber = RubberDuck();

    cout << "\n\n";
    mullard.display();
    mullard.swim();
    mullard.fly();
    mullard.quack();

    cout << "\n\n";
    red_head.display();
    red_head.swim();
    red_head.fly();
    red_head.quack();

    cout << "\n\n";
    decoy.display();
    decoy.swim();
    decoy.fly();
    decoy.quack();

    cout << "\n\n";
    rubber.display();
    rubber.swim();
    rubber.fly();
    rubber.quack();

}