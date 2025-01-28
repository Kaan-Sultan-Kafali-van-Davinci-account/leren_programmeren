import time
from termcolor import colored
from math import ceil
from data import *

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return round(amount / 10, 2)

def silver2gold(amount:int) -> float:
    return round(amount / 5, 2)

def copper2gold(amount:int) -> float:
    return round(copper2silver(amount) / 5, 2)

def platinum2gold(amount:int) -> float:
    return round(amount * 25, 2)

def getPersonCashInGold(personCash:dict) -> float:
    cash = 0
    for resource in personCash:
        if resource == 'copper':
            cash += copper2gold(personCash[resource])
        if resource == 'silver':
            cash += silver2gold(personCash[resource])
        if resource == 'gold':
            cash += personCash[resource]
        if resource == 'platinum':
            cash += platinum2gold(personCash[resource])
    return round(cash, 2)

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    foodCost = COST_FOOD_HUMAN_COPPER_PER_DAY * people
    horsesCost = COST_FOOD_HORSE_COPPER_PER_DAY * horses
    return copper2gold((foodCost + horsesCost) * JOURNEY_IN_DAYS)

##################### O06 #####################

def getFromListByKeyIs(list: list, key: str, value: any) -> list:
    items = []
    for dictionary in list:
        if key in dictionary and dictionary[key] == value:
            items.append(dictionary)
    return items

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends:list) -> list:
    items = []
    for dictionary in friends:
        if dictionary["adventuring"] and dictionary["shareWith"]:
            items.append(dictionary)
    return items

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return ceil(people / 3)

def getTotalRentalCost(horses: int, tents: int) -> float:
    horse_cost = silver2gold(COST_HORSE_SILVER_PER_DAY * horses * JOURNEY_IN_DAYS)
    tent_cost = COST_TENT_GOLD_PER_WEEK * tents * ceil(JOURNEY_IN_DAYS / 7)
    return round(horse_cost + tent_cost, 2)

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    final = ""
    for index, item in enumerate(items):
        final += str(item['amount']) + item['unit'] + " " + item['name']
        if len(items) > 1:
            if index < len(items) - 2:
                final += ', '
            elif index < len(items) - 1:
                final += ' & '
    return final

def getItemsValueInGold(items:list) -> float:
    total = 0
    for item in items:
        if item["price"]["type"] == "copper":
            total += copper2gold(item["price"]["amount"]) * item["amount"]
        if item["price"]["type"] == "silver":
            total += silver2gold(item["price"]["amount"]) * item["amount"]
        if item["price"]["type"] == "gold":
            total += item["price"]["amount"] * item["amount"]
        if item["price"]["type"] == "platinum":
            total += platinum2gold(item["price"]["amount"]) * item["amount"]
    total = round(total, 2)
    return float(total)

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    total = 0.0
    for person in people:
        total += getPersonCashInGold(person["cash"])
    return round(total, 2)

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()