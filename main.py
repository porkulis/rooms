from komnata import *

#main##############################################

#Stworzenie pierwszej komnaty
komnata = Komnata(f"sala wejściowa", 0, f"Znajdują się tutaj potężne drewniane drzwi prowadzące na wschód.")
komnaty.append(komnata)
print(f"\nTworzę komnatę o nazwie: {komnata.name}")
print(len(komnaty))
current_room = komnata  #ustawienie początkowej lokacji gracza

#Stworzenie pozostałych komnat i ścieżek
previous_choice = []
exits_choice = []
for n in range(5):
    create_room()
    exits_options = [["północ", "południe"], ["południe", "północ"], ["wschód", "zachód"], ["zachód", "wschód"]]

    #print(f"previous_choice: {previous_choice}")  # TEST


    while exits_choice == previous_choice:
        i = random.randint(0, 3)
        exits_choice = exits_options[i]

    previous_choice = exits_choice

    print(f"exits_choice: {exits_choice}")  #TEST

    # komnaty[z].exits[exits_choice[0]] = komnaty[z + 1] #wyjscie ze stworzonej komnaty
    # komnaty[z + 1].exits[exits_choice[1]] = komnaty[z] #wyście dla poprzedniej komnaty
    for komnata in komnaty:
        print(f"komnata {komnata.number}")
    print(len(komnaty))


    komnaty[len(komnaty)-1].exits[exits_choice[0]] = komnaty[len(komnaty)-2] #wyjscie ze stworzonej komnaty

    komnaty[len(komnaty)-2].exits[exits_choice[1]] = komnaty[len(komnaty)-1] #wyście dla poprzedniej komnaty

#sys.exit()

print("\n---Lista stworzonych komnat i wyjść:")
i = 0
for n in range(len(komnaty)):
    print(f"{komnaty[i].name}: numer: {komnaty[i].number}")
    #print(f"  Wyścia: {komnaty[i].exits}")
    for key, value in komnaty[i].exits.items():
        if value != None:
            print(f"   - {key}: {value.name}")
    i += 1

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
