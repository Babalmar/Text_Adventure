import os

equipment = ["Flask", "Rusty sword", "Pendant"]

def equipement_list():
    print('Equipment:', ', '.join(equipment))

def display_text(filename):
    with open(filename, 'r') as f:
        text = f.read()
        print(text)
        f.close()


display_text('./Texts/start.txt')
equipement_list()
while True:
    decision = input("Which path will you choose?\n>>> ")
    if decision.lower() not in ('n', 'e', 'w', 's'):
        print("Not an appropriate choice.")
    else:
        break
if decision == 'n':
    os.system('cls')
    print('You went to the forest')
    equipement_list()
elif decision == 'e':
    print('You went to the village')
    equipement_list()
elif decision == 'w':
    print('You went to the swamp')
    equipement_list()
elif decision == 's':
    print('You went to the cemetery')
    equipement_list()