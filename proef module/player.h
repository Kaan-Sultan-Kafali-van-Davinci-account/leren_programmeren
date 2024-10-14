class Player{
        int attack;
        int defense;
        int health;
        int rupees = 0;
        bool key = false;
        bool gotSword = false;
        bool gotShield = false;
        
    public:
    
        Player(int attack, int defense, int health) : attack(attack), defense(defense), health(health){
        }

        setAttack(int attack) {this->attack = attack;}
        setDefense(int defense) {this->defense = defense;}
        setHealth(int health) {this->health = health;}
        setRupees(int rupees) {this->rupees = rupees;}
        setKey(bool key) {this->key = key;}
        setGotSword(bool gotSword) {this->gotSword = gotSword;}
        setGotShield(bool gotShield) {this->gotShield = gotShield;}

        getAttack() {return attack;}
        getDefense() {return defense;}
        getHealth() {return health;}
        getRupees() {return rupees;}
        getKey() {return key;}
        getGotSword() {return gotSword;}
        getGotShield() {return gotShield;}
        
};