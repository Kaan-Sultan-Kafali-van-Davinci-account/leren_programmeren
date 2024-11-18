wachtwoord = "!?KaAnTunA80?!"

attempt = ""
a = 0

while a < 5 and attempt != wachtwoord: attempt = input("Voer wachtwoord: "); a += 1

if attempt == wachtwoord: print("Je gebruikte " + str(a) + " pogingen")
else: print("POGINGEN ZIJN OP...")