#include <iostream>
#include <random>
#include <ctime>
#include <cmath>
#include <windows.h>
#include "player.h"
#include "enemy.h"

//#define print(x) std::cout << x << std::endl;

using namespace std;

void battle(Player* protagonist, Enemy* antagonist, string name_enemy) {
    int zombie_hit_damage = (*antagonist).getAttack() - (*protagonist).getDefense();
    int player_hit_damage = (*protagonist).getAttack() - (*antagonist).getDefense();
    if (zombie_hit_damage <= 0) {cout << "Jij hebt een te goede verdediging voor de " << name_enemy << " , hij kan je geen schade doen." << endl;}
    else {
        int zombie_attack_amount = ceil((*protagonist).getHealth() / zombie_hit_damage);
        int player_attack_amount = ceil((*antagonist).getHealth() / player_hit_damage);

        if (player_attack_amount < zombie_attack_amount) {
            protagonist->setHealth((*protagonist).getHealth() - zombie_hit_damage);
            cout << "HP - " << zombie_hit_damage << endl;
            cout << "In " << player_attack_amount << " rondes versla je de " << name_enemy << "." << endl;
            cout << "Je health is nu " << (*protagonist).getHealth() << "." << endl;}
        else {
            cout << "Helaas is de " << name_enemy << " te sterk voor je." << endl;
            cout << "GAME OVER" << endl;
            Sleep(5000);}
    }
    cout << "" << endl;
    Sleep(1000);
};

int main() {
    random_device rd;
    mt19937 gen(static_cast<unsigned int>(time(0)));

    cout << "Weer meer klanten gewenst\n" << endl;

    Player player1(1, 0, 3);

    cout << "Door de twee grote deuren loop je een gang binnen." << endl;
    cout << "Het ruikt hier muf en vochtig." << endl;
    cout << "Je ziet een deur voor je." << endl;
    cout << "" << endl;

    Sleep(1000);

    uniform_int_distribution<> distr7(1, 10);

    if (distr7(gen) != 10) {
        cout << "Je stapt door de deur heen en je ziet een rupee liggen voor je." << endl;
        cout << "Je pakt het op: RUPEE +1" << endl;
        player1.setRupees(player1.getRupees() + 1);
        }
    else {
        cout << "Deze kamer is betoverd door de wizard, dus er ligt geen rupee" << endl;
        }
    cout << "Je gaat verder en je ziet twee deuren voor je. Een die naar rechts leidt en de ander die naar rechtvoor leidt" << endl;
    cout << "" << endl;

    Sleep(1000);
    cout << "Wil je naar rechts (1) gaan of rechtdoor (2)? Kies uit 1 en 2: " << endl;
    unsigned short int richting;
    unsigned short int richting2;
    unsigned short int richting3;
    unsigned short int richting4;
    cin >> richting;
    cout << "" << endl;    

    if (richting == 2) {

        Sleep(1000);

        cout << "Je stapt door de deur heen en je ziet een standbeeld voor je." << endl;
        cout << "Het standbeeld heeft een rupee vast." << endl;
        cout << "Op zijn borst zit een numpad met de toesten 9 t/m 0." << endl;

        uniform_int_distribution<> distr1(10, 25);
        unsigned short int no1 = distr1(gen);
        uniform_int_distribution<> distr2(-5, 75);
        short int no2 = distr2(gen);
        uniform_int_distribution<> distr3(1, 3);
        unsigned short int operand = distr3(gen);

        if (operand == 1) {
            cout << "Daarboven zie je een som staan: " << no1 << " + " << no2 << " = ?" << endl;
            int answer; cin >> answer;
            if ((int)answer == no1 + no2) {cout << "Het stadbeeld laat de rupee vallen en je pakt het op" << endl; player1.setRupees(player1.getRupees() + 1); cout << "RUPEE +1" << endl;}
            else {cout << "Er gebeurt niets...." << endl;}}
        if (operand == 2) {
            cout << "Daarboven zie je een som staan: " << no1 << " - " << no2 << " = ?" << endl;
            int answer; cin >> answer;
            if ((int)answer == no1 - no2) {cout << "Het stadbeeld laat de rupee vallen en je pakt het op" << endl; player1.setRupees(player1.getRupees() + 1); cout << "RUPEE +1" << endl;}
            else {cout << "Er gebeurt niets...." << endl;}}
        if (operand == 3) {
            cout << "Daarboven zie je een som staan: " << no1 << " * " << no2 << " = ?" << endl;
            int answer; cin >> answer;
            if ((int)answer == no1 * no2) {cout << "Het stadbeeld laat de rupee vallen en je pakt het op" << endl; player1.setRupees(player1.getRupees() + 1); cout << "RUPEE +1" << endl;}
            else {cout << "Er gebeurt niets...." << endl;}}
        
        cout << "Je ziet twee deuren achter het standbeeld." << endl;
        cout << "" << endl;

        Sleep(1000);

        cout << "wil je naar rechts (1) gaan of rechtdoor (2)? Kies uit 1 en 2: " << endl;
        cin >> richting2;

        if (richting2 == 2) {
            Enemy zombie1(1, 2, 0);

            cout << "Je opent de deur en je komt een zombie tegen." << endl;
            cout << "Je loopt tegen een zombie aan." << endl;

            battle(&player1, &zombie1, "zombie");
            if (player1.getHealth() <= 0) {return 0;}

            cout << "" << endl;
            Sleep(1000);
            cout << "Je ziet nog twee deuren. Eentje naar links (1) en eentje rechtsdoor (2)." << endl;
            cout << "Kies tussen 1 en 2..." << endl;
            cin >> richting3;
        }

        Sleep(1000);

        uniform_int_distribution<> distr4(1, 2);
        unsigned short int item_randomizer = distr4(gen);
    }
    
    if (richting3 == 2 or richting2 == 1 or richting == 1) {
        cout << "" << endl;
        cout << "Je duwt hem open en stap een hele lange kamer binnen." << endl;
        Sleep(1000);

        unsigned short int ds;
        cout << "Er zijn twee dobbelstenen, je kan kiezen als je ze wilt rollen." << endl;
        Sleep(500);
        cout << "Als je totaal meer dan 7 krijgt, dan verdubbel je al je rupees." << endl;
        Sleep(500);
        cout << "Als je 7 totaal krijgt, dan krijg je een rupee en 4 hp." << endl;
        Sleep(500);
        cout << "Als je minder dan 7 krijgt verdwijnt een hp." << endl;
        Sleep(500);
        cout << "Wil je dobbelstenen rollen? Ja (1), nee (2)" << endl;
        cin >> ds;
        unsigned short int ds1;
        unsigned short int ds2;
        uniform_int_distribution<> distr5(1, 6);
        uniform_int_distribution<> distr6(1, 6);
        if (ds == 1) {
            ds1 = distr6(gen);
            ds2 = distr6(gen);
            if (ds1 + ds2 > 7) {
                player1.setRupees(player1.getRupees() * 2);
                cout << "Je land een " << ds1 + ds2 << "!" << endl;
                cout << "Jouw rupees gaan verdubbelen. Je hebt nu " << player1.getRupees() << " rupees. RUPEE * 2" << endl;
            }
            if (ds1 + ds2 == 7) {
                player1.setRupees(player1.getRupees() + 1);
                player1.setHealth(player1.getHealth() + 4);
                cout << "Je land een " << ds1 + ds2 << "!" << endl;
                cout << "Je krijgt een extra rupee en 4 hp. Je hebt nu " << player1.getRupees() << " rupees en " << player1.getHealth() << " hp. RUPEE + 1, HP + 4" << endl;
            }
            if (ds1 + ds2 < 7) {
                player1.setHealth(player1.getHealth() - 1);
                cout << "Je land een " << ds1 + ds2 << "..." << endl;
                cout << "Je verliest een hp. Je hebt nu " << player1.getHealth() << " hp. HP - 1" << endl;
                Sleep(2000);
            }
        }

        if (player1.getHealth() <= 0) {
            cout << "Helaas heb je geen levens meer over." << endl;
            cout << "GAME OVER" << endl;
            Sleep(2000);
            return 0;
        }

        
        cout << "Er zijn ook twee deuren, eentje aan de linkerkant en de ander aan de rechterkant." << endl;
        cout << "Kies uit rechts (1), links (2):" << endl;
        cin >> richting4;
        
        Sleep(1000);
        cout << "Je gaat nu de volgende kamer binnentreden." << endl;
    }
        

    if (richting4 == 1) {
        Sleep(1000);
        cout << "De volgende kamer blijkt een betovering te zijn." << endl;
        cout << "Of je krijgt DEFENSE + 1 of je krijgt HP + 2" << endl;
        Sleep(1000);
        cout << "..." << endl;
        Sleep(1000);
        unsigned short int magic;
        uniform_int_distribution<> distr8(1, 2);
        magic = distr8(gen);
        if (magic == 1) {cout << "DEFENSE + 1" << endl; player1.setDefense(player1.getDefense() + 1);}
        if (magic == 2) {cout << "HP + 2" << endl; player1.setHealth(player1.getHealth() + 2);}
        }

    Sleep(1000);

    string item = "";
    unsigned short int picked_item;
    while (player1.getRupees() > 0) {
        cout << "In deze kamer staat een merchant, je ziet een tafel met daarop een zwaard, schild en sleutel. Alle drie kosten 1 rupee." << endl;
        Sleep(1000);
        cout << "Kies je zwaard (1) of kies je schild (2) of kies je sleutel (3) of pass (4)? Kies uit 1, 2, 3 en 4: " << endl;
        cin >> picked_item;
        
        if (picked_item == 1 && player1.getRupees() >= 1) {
            if (!player1.getGotSword()) {
                item = "zwaard"; 
                player1.setAttack(player1.getAttack() + 2); 
                cout << "Je pakt het " << item << " op en houd het bij je. Je hebt een rupee besteden. RUPEE -1, ATTACK + 2" << endl; 
                player1.setRupees(player1.getRupees() - 1); 
                player1.setGotSword(true);
            } else {
                cout << "De zwaard heb je al!" << endl;
            }
        } else if (picked_item == 2 && player1.getRupees() >= 1) {
            if (!player1.getGotShield()) {
                item = "schild"; 
                player1.setDefense(player1.getDefense() + 1); 
                cout << "Je pakt het " << item << " op en houd het bij je. Je hebt een rupee besteden. RUPEE -1, DEFENSE + 1" << endl; 
                player1.setRupees(player1.getRupees() - 1); 
                player1.setGotShield(true);
            } else {
                cout << "De schild heb je al!" << endl;
            }
        } else if (picked_item == 3 && player1.getRupees() >= 1) {
            if (!player1.getKey()) {
                item = "sleutel"; 
                cout << "Je pakt het " << item << " op en houd het bij je. Je hebt een rupee besteden. RUPEE -1, KEY OBTAINED!" << endl; 
                player1.setKey(true); 
                player1.setRupees(player1.getRupees() - 1);
            } else {
                cout << "De sleutel heb je al!" << endl;
            }
        } else if (picked_item == 4) {
            cout << "Pass." << endl;
            break
        }
        
        if (player1.getRupees() < 1) {
            cout << "Je hebt geen rupee meer over." << endl;
            break
        }
    }
    cout << "Op naar de volgende deur." << endl;
    cout << "" << endl;

    Sleep(3000);

    Enemy ork1(2, 0, 3);

    if (item != "") {cout << "Dapper met je nieuwe " << item << " loop je de kamer binnen." << endl;}
    else {cout << "Dapper loop je de kamer binnen." << endl;}
    cout << "Je loopt tegen een ork aan. Hij ziet er sterker uit dan de zombie van daarvoor." << endl;

    battle(&player1, &ork1, "ork");
    if (player1.getHealth() <= 0) {return 0;}
    cout << "" << endl;

    Sleep(1000);

    cout << "Voorzichtig open je de deur." << endl;
    cout << "Tot je verbazig zie je een schatkist in het midden van de kamer staan." << endl;
    cout << "Je loopt er naartoe." << endl;
    cout << "" << endl;

    Sleep(1000);

    if (player1.getKey()) {
        cout << "Met je sleutel doe je de schatkist open." << endl;
        cout << "Je hebt heel veel goud gevonden!" << endl;
        cout << "YOU WIN" << endl;}
    else {
        cout << "Je blijkt geen sleutel te hebben om de schatkist te openen." << endl;
        cout << "GAME OVER" << endl;}

    

    Sleep(1000);

    string last_words;
    cin >> last_words;

    return 0;
}