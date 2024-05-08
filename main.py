from komnata import *
import time


#main##############################################
clear()
# print("\nWitaj w grze \"Arena Śmierci VII\"\n")
# time.sleep(3)

def create_room():
    komnata = Komnata(f"{create_name()}", len(komnaty), f"{create_description()}.")
    komnaty.append(komnata)

def change_room(room):
    current_room = komnaty[room]

    possible_exits = []
    clear()
    print(f"Znajdujesz się w: [Komnata {current_room.number}] - '{current_room.name.title()}' - Licznik komnat: ({current_room.number}/{(len(komnaty)-1)}) By zakończyć grę wciśnij \"q\"")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    print(f"Twoim oczom ukazuje się {current_room.name.title()}.")
    print(f"  {current_room.description}")

    if current_room not in visited_rooms:
        print("\nJesteś tu po raz pierwszy.")
    else:
        print("\nJuż tu byłeś.")
    if current_room not in visited_rooms:
        visited_rooms.append(current_room)

    print("\nMożliwe wyjścia:")
    numerator = 1
    goback = 0
   
    if dest == "północ":
        goback = "południe"
    elif dest == "południe":
        goback = "północ"
    elif dest == "zachód":
        goback = "wschód"
    elif dest == "wschód":
        goback = "zachód"

    for key, value in current_room.exits.items():
        if value != None:
            if key == goback:
                print(f"  <--powrót {numerator}. {key}: {value.name.title()} (Komnata {value.number})")
            else:
                print(f"  dalej---> {numerator}. {key}: {value.name.title()} (Komnata {value.number})")
            numerator += 1
        else:
            print(f"            {numerator}. {key}: x")
            numerator += 1
    return current_room

#Stworzenie pierwszej komnaty
komnata = Komnata(f"Komnata z Drzwiami", 0, f"Znajdują się tutaj potężne drewniane drzwi prowadzące do labiryntu.")
komnaty.append(komnata)
current_room = komnata  #ustawienie początkowej lokacji gracza



#Stworzenie pozostałych komnat i ścieżek

#-------------------------------------------------------------------------------------------------------------
previous_choice = [1]
exits_choice = [1]

for n in range(2):
    create_room()

    exits_options = [["północ", "południe"], ["południe", "północ"], ["wschód", "zachód"], ["zachód", "wschód"]]

    if len(komnaty) <= 2:
        exits_choice = exits_options[0]
        previous_choice = exits_choice
    elif len(komnaty) > 2:
        exits_choice = exits_options[random.randint(0, 3)]
        while previous_choice[1] == exits_choice[0]:
            exits_choice = exits_options[random.randint(0, 3)]
    if previous_choice[1] == exits_choice[0]:
        print("ERRRRRRRRRROOOOOOOOOOOR")  
    previous_choice = exits_choice



    komnaty[len(komnaty)-2].exits[exits_choice[0]] = komnaty[len(komnaty)-1] #wyjscie ze stworzonej komnaty

    komnaty[len(komnaty)-1].exits[exits_choice[1]] = komnaty[len(komnaty)-2] #wyście dla poprzedniej komnaty
#-------------------------------------------------------------------------------------------------------------

#sys.exit()

# print("\n---Lista stworzonych komnat i wyjść:")
# i = 0
# for n in range(len(komnaty)):
#     #print(f"{komnaty[i].name}: numer: {komnaty[i].number}")
#     print(f"Komnata {komnaty[i].number}")
#     #print(f"  Wyścia: {komnaty[i].exits}")
#     for key, value in komnaty[i].exits.items():
#         # if value != None:
#         #     print(f"   - {key}: Komnata {value.number}")
#         # else:
#         #     print(f"   - {key}: {value}")
#         if value != None:
#             print(f"   - {key}: Komnata {value.number}")
#     i += 1

#sys.exit()
dest = 0
current_room = change_room(0)
last_dest = []
while True:
    directions = []
    possible_exits = {}
    for key, value in current_room.exits.items():
        if value != None:
            n = komnaty.index(value)
            directions.append(key)
            possible_exits[key] = komnaty.index(value)

    dest = choose_direction()

    if dest not in directions:
        print(f"Na {dest} jest lita ściana.")
    elif dest in directions:
        print(f"Ruszasz na {dest}.")
        current_room = change_room(int(possible_exits[dest]))
    #print(f"\nLicznik komnat: ({current_room.number}/{(len(komnaty)-1)})")

    #if current_room.number == len(komnaty)-1:
    if current_room not in visited_rooms[:-1]:
        #print("Tworzę nową komnatę.")
        create_room()

        exits_options = [["północ", "południe"], ["południe", "północ"], ["wschód", "zachód"], ["zachód", "wschód"]]

        if len(komnaty) <= 2:
            exits_choice = exits_options[0]
            previous_choice = exits_choice
        elif len(komnaty) > 2:
            exits_choice = exits_options[random.randint(0, 3)]
            while previous_choice[1] == exits_choice[0]:
                exits_choice = exits_options[random.randint(0, 3)]
        if previous_choice[1] == exits_choice[0]:
            print("ERRRRRRRRRROOOOOOOOOOOR")  
        previous_choice = exits_choice

        komnaty[len(komnaty)-2].exits[exits_choice[0]] = komnaty[len(komnaty)-1] #wyjscie ze stworzonej komnaty
        komnaty[len(komnaty)-1].exits[exits_choice[1]] = komnaty[len(komnaty)-2] #wyście dla poprzedniej komnaty
