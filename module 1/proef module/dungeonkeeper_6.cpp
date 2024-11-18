#include <iostream>
#include <random>
#include <ctime>
#include <cmath>
#include <windows.h>
#include "player.h"
#include "zombie.h"

using namespace std;

int main() {
    random_device rd;
    mt19937 gen(static_cast<unsigned int>(time(0)));

    cout << "Voor de gokker\n" << endl;

    Player player1(1, 0, 3);

    cout << "Door de twee grote deuren loop je een gang binnen." << endl;
    cout << "Het ruikt hier muf en vochtig." << endl;
    cout << "Je ziet een deur voor je." << endl;
    cout << "" << endl;

    Sleep(1000);

    cout << "Je stapt door de deur heen en je ziet een rupee liggen voor je." << endl;
    cout << "Je pakt het op: RUPEE +1" << endl;
    player1.setRupees(player1.getRupees() + 1);
    cout << "Je gaat verder en je ziet twee deuren voor je. Een die naar rechts leidt en de ander die naar rechtvoor leidt" << endl;
    cout << "" << endl;

    Sleep(1000);
    cout << "Wil je naar rechts (1) gaan of rechtdoor (2)? Kies uit 1 en 2: " << endl;
    unsigned short int richting; cin >> richting;
    cout << "" << endl;

    if (richting == 2) {

        Sleep(1000);

        cout << "Je stapt door de deur heen en je ziet een standbeeld voor je." << endl;
        cout << "Het standbeeld heeft een sleutel vast." << endl;
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
            if ((int)answer == no1 + no2) {cout << "Het stadbeeld laat de sleutel vallen en je pakt het op" << endl; player1.setKey(true);}
            else {cout << "Er gebeurt niets...." << endl;}}
        if (operand == 2) {
            cout << "Daarboven zie je een som staan: " << no1 << " - " << no2 << " = ?" << endl;
            int answer; cin >> answer;
            if ((int)answer == no1 - no2) {cout << "Het stadbeeld laat de sleutel vallen en je pakt het op" << endl; player1.setKey(true);}
            else {cout << "Er gebeurt niets...." << endl;}}
        if (operand == 3) {
            cout << "Daarboven zie je een som staan: " << no1 << " * " << no2 << " = ?" << endl;
            int answer; cin >> answer;
            if ((int)answer == no1 * no2) {cout << "Het stadbeeld laat de sleutel vallen en je pakt het op" << endl; player1.setKey(true);}
            else {cout << "Er gebeurt niets...." << endl;}}
        
        cout << "Je ziet twee deuren achter het standbeeld." << endl;
        cout << "" << endl;

        Sleep(1000);

        cout << "wil je naar rechts (1) gaan of rechtdoor (2)? Kies uit 1 en 2: " << endl;
        unsigned short int richting2; cin >> richting2;

        if (richting2 == 2) {
            Zombie zombie1(1, 2, 0);

            cout << "Je opent de deur en je komt een zombie tegen." << endl;
            cout << "Je loopt tegen een zombie aan." << endl;

            int zombie_hit_damage = zombie1.getAttack() - player1.getDefense();
            int player_hit_damage = player1.getAttack() - zombie1.getDefense();
            if (zombie_hit_damage <= 0) {cout << "Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen." << endl;}
            else {
                int zombie_attack_amount = ceil(player1.getHealth() / zombie_hit_damage);
                int player_attack_amount = ceil(zombie1.getHealth() / player_hit_damage);

                player1.setHealth(player1.getHealth() - zombie_hit_damage);

                if (player_attack_amount < zombie_attack_amount and player1.getHealth() > 0) {
                    cout << "In " << player_attack_amount << " rondes versla je de zombie." << endl;
                    cout << "Je health is nu " << player1.getHealth() << "." << endl;}
                else {
                    cout << "Helaas is de ork te sterk voor je." << endl;
                    cout << "GAME OVER" << endl;
                    Sleep(1000);
                    return 0;}
            }
            cout << "" << endl;
            Sleep(1000);
            cout << "Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen." << endl;
        }

        Sleep(1000);

        uniform_int_distribution<> distr4(1, 2);
        unsigned short int item_randomizer = distr4(gen);
    }

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
            cout << "Jouw rupees gaan verdubbelen. Je hebt nu " << player1.getRupees() << " rupees." << endl;
        }
        if (ds1 + ds2 == 7) {
            player1.setRupees(player1.getRupees() + 1);
            player1.setHealth(player1.getHealth() + 4);
            cout << "Je land een " << ds1 + ds2 << "!" << endl;
            cout << "Je krijgt een extra rupee en 4 hp. Je hebt nu " << player1.getRupees() << " rupees en " << player1.getHealth() << " hp." << endl;
        }
        if (ds1 + ds2 < 7) {
            player1.setHealth(player1.getHealth() - 1);
            cout << "Je land een " << ds1 + ds2 << "..." << endl;
            cout << "Je verliest een hp. Je hebt nu " << player1.getHealth() << " hp." << endl;
            Sleep(2000);
        }
    }

    if (player1.getHealth() <= 0) {
        cout << "Helaas heb je geen levens meer over." << endl;
        cout << "GAME OVER" << endl;
        Sleep(2000);
        return 0;
    }
    
    Sleep(1000);
    cout << "Je gaat nu de volgende kamer binnentreden." << endl;
    Sleep(1000);

    string item = "";
    unsigned short int picked_item;
    while (player1.getRupees() > 0) {
        cout << "In deze kamer staat een merchant, je ziet een tafel met daarop een zwaard en schild, allebei kosten 1 rupee." << endl;
        Sleep(1000);
        cout << "Kies je zwaard (1) of kies je schild (2) of pass (3)? Kies uit 1, 2 en 3: " << endl;
        cin >> picked_item;
        
        if (picked_item == 1 and player1.getRupees() >= 1) {item = "zwaard"; player1.setAttack(player1.getAttack() + 2); cout << "Je pakt het " << item << " op en houd het bij je. Je hebt een rupee besteden. RUPEE -1" << endl; player1.setRupees(player1.getRupees() - 1);}
        if (picked_item == 2 and player1.getRupees() >= 1) {item = "schild"; player1.setDefense(player1.getDefense() + 1); cout << "Je pakt het " << item << " op en houd het bij je. Je hebt een rupee besteden. RUPEE -1" << endl; player1.setRupees(player1.getRupees() - 1);}
        if (picked_item == 3) {cout << "Pass." << endl; break;}
        if (player1.getRupees() < 1) {cout << "Je hebt geen rupee meer over." << endl; break;}
        }
    cout << "Op naar de volgende deur." << endl;
    cout << "" << endl;

    Sleep(3000);

    Zombie ork1(2, 0, 3);

    if (item != "") {cout << "Dapper met je nieuwe " << item << " loop je de kamer binnen." << endl;}
    else {cout << "Dapper loop je de kamer binnen." << endl;}
    cout << "Je loopt tegen een ork aan. Hij ziet er sterker uit dan de zombie van daarvoor." << endl;

    int ork_hit_damage = ork1.getAttack() - player1.getDefense();
    int player_hit_damage2 = player1.getAttack() - ork1.getDefense();
    if (ork_hit_damage <= 0) {cout << "Jij hebt een te goede verdediging voor de ork, hij kan je geen schade doen." << endl;}
    else {
        int ork_attack_amount = ceil(player1.getHealth() / ork_hit_damage);
        int player_attack_amount2 = ceil(ork1.getHealth() / player_hit_damage2);

        player1.setHealth(player1.getHealth() - ork_hit_damage);

        if (player_attack_amount2 < ork_attack_amount and player1.getHealth() > 0) {
            cout << "In " << player_attack_amount2 << " rondes versla je de ork." << endl;
            cout << "Je health is nu " << player1.getHealth() << "." << endl;}
        else {
            cout << "Helaas is de ork te sterk voor je." << endl;
            cout << "GAME OVER" << endl;
            Sleep(1000);
            return 0;}
    }
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