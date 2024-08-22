#ifndef DUCK  
#define DUCK

// Quackable interface
/*
methods:
    + quack()
*/
// virtual void Quackable::quack(); 

class Quackable {
    public:
        virtual void quack(); 
};

// concrete Quackable behaviours: Quack, Squeak, Mute

class Quack : public Quackable {
    public:
        void quack();
};


class Squeak : public Quackable {
    public:
        void quack();
};


class Mute : public Quackable {
    public:
        void quack();
};


// Flyable interface
/*
methods:
    + fly()
*/

class Flyable {
    public:
        virtual void fly(); 
};


// concrete flyable behaviours: fly with wings, non-flyable

class FlyWithWings : public Flyable {
    public:
        void fly();
};

class FlyNoWay : public Flyable {
    public:
        void fly();
};

// abstract class Duck
/*
has: 
    - Quackable qb
    - Flyable fb
behaviour:
    + fly()
    + quack()
    + display()
    + swim()
    + set_quackable_behaviour()
    + set_flyable_behaviour()
*/
class Duck {
    protected:
        Quackable *quackable_behaviour;
        Flyable *flyable_behaviour;
    public:
        virtual void fly();
        virtual void quack();
        virtual void swim();
        virtual void display();
        void set_quackable_behaviour(Quackable *qb);
        void set_flyable_behaviou(Flyable *fb);
};

// concrete Ducks: Mullard, RedHead, Rubber, Decoy
class MullardDuck : public Duck {
    public:
        MullardDuck();
        void fly();
        void quack();
        void swim();
        void display();
};


class RedHeadDuck : public Duck {
    public:
        RedHeadDuck();
        void fly();
        void quack();
        void swim();
        void display();
};


class RubberDuck : public Duck {
    public:
        RubberDuck();
        void fly();
        void quack();
        void swim();
        void display();
};

class Decoy : public Duck {
    public:
        Decoy();
        void fly();
        void quack();
        void swim();
        void display();
};
#endif