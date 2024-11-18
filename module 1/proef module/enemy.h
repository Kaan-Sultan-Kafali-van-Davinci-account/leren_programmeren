class Enemy{
    int attack;
    int defense;
    int health;
    
    public:
        Enemy(int attack, int defense, int health) : attack(attack), health(health), defense(defense){
        }

        setAttack(int attack) {this->attack = attack;}
        setDefense(int defense) {this->defense = defense;}
        setHealth(int health) {this->health = health;}

        getAttack() {return attack;}
        getDefense() {return defense;}
        getHealth() {return health;}
};