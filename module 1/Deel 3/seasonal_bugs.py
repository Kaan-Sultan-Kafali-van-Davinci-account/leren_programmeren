print('Welk seizoen vind jij het fijnst?', 
      "\nA) Lente", 
      "\nB) Zomer", 
      "\nC) Herfst", 
      "\nD) Winter")
gekozen_seizoen = input('? ').lower()

if (gekozen_seizoen == 'a' or gekozen_seizoen == 'c'):
    print('Dus jij vindt een tussenseizoen het fijnst...')
elif (gekozen_seizoen == 'b'):
    weer_type = 'warm'
    print(f'Dus jij houd van {weer_type} weer!')
else:
    weer_type = 'koud'
    print(f'Dus jij houd van {weer_type} weer!')