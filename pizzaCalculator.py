#Cedric Francis Pizza calculator 
keuzePizza = input("---------------------------------------------------" + "\n" #Keuze menu van afmetingen (\n voor een nieuwe regel)
"|  Type welke afmeting pizza u wilt: "  + "\n"            
"|  Small:€6.99  " + "\n"        
"|  Medium:€9.99 " + "\n"                 
"|  Large:€14.99 " +"\n"                     
"---------------------------------------------------" + "\n"
)

if keuzePizza.lower().strip() == ("small"): #keuzePizza wordt omgezet in lowercase en er wordt gecheckt of het "small"
    prijsPizza = float(6.99) #prijs van de pizza wordt aangegeven
    hoeveelPizza = int(input("Hoeveel pizza wil je?: ")) #hoeveelheid wordt gevraagd in integer voor de berekening en zodat niemand een onveven pizza besteld
elif keuzePizza.lower().strip() == ("medium"):
    prijsPizza = float(9.99)
    hoeveelPizza = int(input("Hoeveel pizza wil je?: "))
elif keuzePizza.lower().strip() == ("large"):
    prijsPizza =float(14.99)
    hoeveelPizza = int(input("Hoeveel pizza wil je?: "))
else: print("Invalid Option") #geen keuze uit de 3 is een invalid option

print("De afmeting die u heeft gekozen was " + keuzePizza + " De hoeveelheid pizza die u heeft gekozen is " + str(hoeveelPizza))
berekeningPizza = prijsPizza * hoeveelPizza #de berekening om de totaale prijs uit te rekenen
print("De prijs wordt intotaal: " + str(berekeningPizza))