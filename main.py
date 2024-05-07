from komnata import *

#main##############################################
print("\nWitaj w grze \"Arena Śmierci VII\"\n")

#Stworzenie pierwszej komnaty
komnata = Komnata(f"sala wejściowa", 0, f"Znajdują się tutaj potężne drewniane drzwi prowadzące wgłąb labiryntu.")
komnaty.append(komnata)
# print(f"\nTworzę komnata {komnata.number}") #Test
# print(f"len(komnaty) = {len(komnaty)}") #Test
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
        #print(f"{exits_choice} Komnata {len(komnaty)-1}") #Test
        previous_choice = exits_choice
    elif len(komnaty) > 2:
        exits_choice = exits_options[random.randint(0, 3)]
        #print(f"{exits_choice} Komnata {len(komnaty)-1}") #Test
        # if previous_choice[1] == exits_choice[0]:
        #     print("ERRRRRRRRRROOOOOOOOOOOR")
        while previous_choice[1] == exits_choice[0]:
            exits_choice = exits_options[random.randint(0, 3)]
            #print(f"{exits_choice} Komnata {len(komnaty)-1}") #Test
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

current_room = change_room(0)
#print(f"\n\nCurrent room: {current_room.name}")
#print(current_room.exits)

while True:
    directions = []
    possible_exits = {}
    for key, value in current_room.exits.items():
        if value != None:
            #print(f"kierunek: {key}, nazwa: {value.name}, index: {komnaty.index(value)}, instancja: {value}")
            n = komnaty.index(value)
            directions.append(key)
            possible_exits[key] = komnaty.index(value)
    #print(directions)
    #print(possible_exits)

    dest = choose_direction()

    if dest not in directions:
        print(f"Na {dest} jest lita ściana.")
    elif dest in directions:
        print(f"Ruszasz na {dest}.")
        current_room = change_room(int(possible_exits[dest]))
    print(f"\nLicznik komnat: ({current_room.number}/{(len(komnaty)-1)})")
    #print(current_room)
    #print(visited_rooms)

    #if current_room.number == len(komnaty)-1:
    if current_room not in visited_rooms[:-1]:
        print("Tworzę nową komnatę.")
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
