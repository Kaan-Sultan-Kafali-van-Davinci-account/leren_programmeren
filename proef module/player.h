class Player{
    public:
        int attack;
        int defense;
        int health;
        int rupees = 0;
        bool key = false;
    
        Player(int attack, int defense, int health) : attack(attack), defense(defense), health(health){
        }

        setAttack(int attack) {this->attack = attack;}
        setDefense(int defense) {this->defense = defense;}
        setHealth(int health) {this->health = health;}
        setRupees(int rupees) {this->rupees = rupees;}
        setKey(bool key) {this->key = key;}

        getAttack() {return attack;}
        getDefense() {return defense;}
        getHealth() {return health;}
        getRupees() {return rupees;}
        getKey() {return key;}
};