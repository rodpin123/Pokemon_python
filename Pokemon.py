print ("Começa a luta entre Pokemon Alpha e Pokemon Bravo!")


def attack(ataque):
       
    while (ataque < 1 or ataque > 4):
        try:
            print ("\nEscolha um ataque e uma defesa!\n 1) Fogo\n 2) Água\n 3) Elétrico\n 4) Físico")
            ataque = int(input("\nSelecione seu ataque (1 a 4) : "))
            if (ataque < 1 or ataque > 4):
                print("\nAtaque não válido, selecione outro!")
                print ("Escolha um ataque!\n 1) Fogo\n 2) Água\n 3) Elétrico\n 4) Físico")
        except ValueError:
            print("\nAtaque não válido, selecione outro!")
            print ("Escolha um ataque!\n 1) Fogo\n 2) Água\n 3) Elétrico\n 4) Físico")
            pass

    if (ataque == 1):
        ataque_tipo = "Fogo!"
    elif (ataque == 2):
        ataque_tipo = "Água!"
    elif (ataque == 3):
        ataque_tipo = "Elétrico!"
    elif (ataque == 4):
        ataque_tipo = "Físico!"
    return(ataque, ataque_tipo)

def defense(defesa):
    
    while (defesa < 1 or defesa > 4):
        try:
            defesa = int(input("\nSelecione sua defesa (1 a 4) : "))
            if (defesa < 1 or defesa > 4):
                print("\nDefesa não válida, selecione outra!")
                print ("Escolha uma defesa!\n 1) Fogo\n 2) Água\n 3)Elétrico\n 4) Físico")
        except ValueError:
            print("\nDefesa não válida, selecione outra!")
            print ("Escolha uma defesa!\n 1) Fogo\n 2) Água\n 3) Elétrico\n 4) Físico")
            pass

    if (defesa == 1):
        defesa_tipo = "Fogo!"
    elif (defesa == 2):
        defesa_tipo = "Água!"
    elif (defesa == 3):
        defesa_tipo = "Elétrico!"
    elif (defesa == 4):
        defesa_tipo =  "Físico!"
    return(defesa, defesa_tipo)

import random

turno = 1
ataque = 0
defesa = 0

vida = 100
vida_oponente = 100

while (vida > 0 and vida_oponente > 0):
    print("\nTurno: ", turno)
    ataque_usado = attack(ataque)
    defesa_usada = defense(defesa)
    ataque_pc = attack(random.randint(1,4))
    defesa_pc = defense(random.randint(1,4))

    
    attack_matrix = [[0, 3, 2, 1],[2, 0, 3, 1], [3, 2, 0, 1], [1, 1, 1, 0]]

    vida_oponente = vida_oponente - (attack_matrix[defesa_pc[0]-1][ataque_usado[0]-1] * 10)
    vida = vida - (attack_matrix[defesa_usada[0]-1][ataque_pc[0]-1] * 10)

    print("\nVocê atacou com ", ataque_usado[1])
    print("Adversário defendeu com ", defesa_pc[1])
    if (attack_matrix[defesa_pc[0]-1][ataque_usado[0]-1] == 3):
        print("-- Oh! É super-efetivo!")
    elif(attack_matrix[defesa_pc[0]-1][ataque_usado[0]-1] == 2):
            print("-- Ataque forte!")
    elif(attack_matrix[defesa_pc[0]-1][ataque_usado[0]-1] == 1):
            print("-- Acertou!")
    elif(attack_matrix[defesa_pc[0]-1][ataque_usado[0]-1] == 0):
            print("-- Errou! Não causou dano!")
    print("\nAdversário atacou com ", ataque_pc[1])
    print("Você defendeu com ", defesa_usada[1])
    if (attack_matrix[defesa_usada[0]-1][ataque_pc[0]-1] == 3):
        print("-- Oh! É super efetivo!")
    elif(attack_matrix[defesa_usada[0]-1][ataque_pc[0]-1] == 2):
            print("-- Ataque forte!")
    elif(attack_matrix[defesa_usada[0]-1][ataque_pc[0]-1] == 1):
            print("-- Acertou!")
    elif(attack_matrix[defesa_usada[0]-1][ataque_pc[0]-1] == 0):
            print("-- Errou! Não causou dano!")


    print("\nDano causado: ",  attack_matrix[defesa_pc[0]-1][ataque_usado[0]-1] * 10) 
    print("Dano recebido: ", attack_matrix[defesa_usada[0]-1][ataque_pc[0]-1] * 10)
    print("Sua vida: ", vida)
    print("Vida oponente: ", vida_oponente)

    turno += 1

    if (vida <= 0 and vida_oponente > 0):
        print("----------------------------------\nPERDEU! Seu Pokemon foi derrotado!\n----------------------------------")
    
    if(vida_oponente <= 0 and vida > 0):
        print("----------------------------------\nPARABÉNS! Você derrotou seu oponente!\n----------------------------------") 

    if (vida <= 0 and vida_oponente <= 0):
        print("----------------------------------\nEMPATOU! Ambos derrotados!\n----------------------------------")
