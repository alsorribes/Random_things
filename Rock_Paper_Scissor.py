import random

print()
print("Benvingut al pedra paper tisora!\n")
print("Les regles són les següents: \n")
print("Has de triar entre un número entre 1 i 3 (1-Pedra / 2-Paper / 3-Tisora)")
print("La pedra guanya a la tisora, el paper guanya a la pedra i la tisora guanya al paper, en cas que surti el mateix, serà empat")
print("La màquina triarà un número aleatori. Si es compleix alguna de les condicions anteriors, guanyes")
print()

def random_number():
    x = random.randint(1,3)
    return x

cont_jug = 0
cont_ia = 0

opcions =  {'1':'PEDRA',
            '2':'PAPER', 
            '3':'TISORA'}

while True:
    x = input("Introdueix un número entre 1 i 3: (1-Pedra / 2-Paper / 3-Tisora) ")
    while int(x) > 3 or int(x) < 1:
        x = input("Introdueix un número entre 1 i 3: (1-Pedra / 2-Paper / 3-Tisora) ")
    y = str(random_number())

    print("Has triat "+opcions.get(x))
    print("La màquina ha triat "+opcions.get(y))
    
    if x != y:
        if int(x) == 3 and int(y) == 1:
            print("Guanya la màquina")
            cont_ia += 1
        elif int(x) == 1 and int(y) == 3:
            print("Has guanyat!")
            cont_jug += 1
        elif x > y:
            print("Has guanyat!")
            cont_jug += 1
        else:
            print("Guanya la màquina!")
            cont_ia += 1
    else:
        print("Empat! Tornem-hi")
    
    print("Marcador:    Jugador --> "+str(cont_jug)+ "     Màquina --> "+str(cont_ia))
    if cont_jug == cont_ia:
        print("Aneu empatats a punts!")
    elif cont_jug > cont_ia:
        print("Vas guanyant!")
    else:
        print("Vas perdent!")
    
    sortida = input("Si vols sortir del joc apreta el 0, si vols seguir apreta l'1: ")
    while int(sortida) > 1 or int(sortida) < 0:
        sortida = input("Si vols sortir del joc apreta el 0, si vols seguir apreta l'1: ")

    print("\n")
    if int(sortida) == 0:
        if cont_jug > cont_ia:
            exit("El guanyador ha estat el jugador!")
        else:
            exit("El guanyador ha estat la màquina!")