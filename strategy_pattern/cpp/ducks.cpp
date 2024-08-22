#include "ducks.h"
#include <iostream>

using namespace std;

// Quackable implementation

void Quack::quack() {
    cout << "Quack!" << endl;
}


void Squeak::quack() {
    cout << "Squeak!" << endl;
}


void Mute::quack() {
    cout << "..." << endl;
}


// Flyable implementation

void FlyWithWings::fly() {
    cout << "Phuuuu, phuuuuu (imitating wings sound)" << endl;
}

void FlyNoWay::fly() {
    cout << "Cannot fly..." << endl;
}


// abstract Duck functionality

void Duck::set_quackable_behaviour(Quackable *qb) {
    quackable_behaviour = qb;
}

void Duck::set_flyable_behaviou(Flyable *fb) {
    flyable_behaviour = fb;
}

// concrete ducks functionality implementation


MullardDuck::MullardDuck() {
    quackable_behaviour = new Quack();
    flyable_behaviour = new FlyWithWings();
}

void MullardDuck::fly() {
    flyable_behaviour->fly();
}

void MullardDuck::quack() {
    quackable_behaviour->quack();
}

void MullardDuck::swim() {
    cout << "Mullard duck is swimming..." << endl;
}

void MullardDuck::display() {
    cout << "Meet a mullard duck!" << endl;
}


RedHeadDuck::RedHeadDuck() {
    quackable_behaviour = new Quack();
    flyable_behaviour = new FlyWithWings();
}

void RedHeadDuck::fly() {
    flyable_behaviour->fly();
}

void RedHeadDuck::quack() {
    quackable_behaviour->quack();
}

void RedHeadDuck::swim() {
    cout << "Red head duck is swimming..." << endl;
}

void RedHeadDuck::display() {
    cout << "Meet a red head duck!" << endl;
}


RubberDuck::RubberDuck() {
    quackable_behaviour = new Squeak();
    flyable_behaviour = new FlyNoWay();
}

void RubberDuck::fly() {
    flyable_behaviour->fly();
}

void RubberDuck::quack() {
    quackable_behaviour->quack();
}

void RubberDuck::swim() {
    cout << "Rubber duck is swimming..." << endl;
}

void RubberDuck::display() {
    cout << "I am entirely yours to listen. What's the problem?" << endl;
}


Decoy::Decoy() {
    quackable_behaviour = new Mute();
    flyable_behaviour = new FlyNoWay();
}

void Decoy::fly() {
    flyable_behaviour->fly();
}

void Decoy::quack() {
    quackable_behaviour->quack();
}

void Decoy::swim() {
    cout << "Decoy duck is swimming..." << endl;
}

void Decoy::display() {
    cout << "Fish, come up!" << endl;
}

