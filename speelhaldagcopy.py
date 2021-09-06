tickets = int(input("Vul hier in hoeveel tickets je hebt: "))
vrbrilmin = int(input("Vul hier in hoeveel minuten je op de vrbril zit: "))
b = (tickets * 7.45) + (vrbrilmin/5 *  0.37)
print(int(b))
if b == (44.44):
    print('Dit geweldige dagje-uit met '+ str(tickets) + ' mensen in de Speelhal met ' + str(vrbrilmin) + ' minuten VR kost je maar ' + str(b) + ' euro')