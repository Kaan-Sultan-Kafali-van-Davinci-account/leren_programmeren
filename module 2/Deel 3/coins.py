# name of student: Kaan
# number of student: 
# purpose of program: 
# structure of program: 

coinValues = [50, 20, 10, 5, 2, 1] #Maak lijst can elke muntsoort
coinTypeReturned = {50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

toPay = int(float(input('Amount to pay: ')) * 100) #Vragen voor invoer
paid = int(float(input('Paid amount: ')) * 100) #Vragen voor invoer
change = paid - toPay #invoer 2 - invoer 1

while change > 0 and len(coinValues) > 0: #

  coinValue = coinValues.pop(0) #stel coinValue naar eerste index van die ene lijst en verwijder
  nrCoins = change // coinValue #

  if nrCoins > 0: #
    print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
    coinTypeReturned[coinValue] = nrCoinsReturned
    change -= nrCoinsReturned * coinValue #

if change > 0:
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
print('Amounts of coin types returned', coinTypeReturned)