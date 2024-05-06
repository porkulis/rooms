from komnata import *
#main##############################################

#Stworzenie pierwszej komnaty
komnata = Komnata(f"sala wejściowa", 0, f"Znajdują się tutaj potężne drewniane drzwi prowadzące na wschód.")
komnaty.append(komnata)
current_room = komnata #ustawienie początkowej lokacji gracza

#Stworzenie pozostałych komnat i ścieżek
z = 0
for n in range(100):
    create_room()
    i = random.randint(1,2)
    if i == 1:
        komnaty[z].exits["wschód"] = komnaty[z+1] 
        komnaty[z+1].exits["zachód"] = komnaty[z]
    else:
        komnaty[z].exits["północ"] = komnaty[z+1] 
        komnaty[z+1].exits["południe"] = komnaty[z]
    z += 1

# print("\n---Lista stworzonych komnat i wyjść:")
# i = 0
# for n in range(len(komnaty)):
#     print(f"{komnaty[i].name}: numer: {komnaty[i].number}, {komnaty[i].description}")
#     print(f"  Wyścia: {komnaty[i].exits}")
#     i += 1

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
            possible_exits[key]=komnaty.index(value)
    #print(directions)
    #print(possible_exits)

    dest = choose_direction()

    if dest not in directions:
        print(f"Na {dest} jest lita ściana.")
    elif dest in directions:
        print(f"Ruszasz na {dest}.")
        current_room = change_room(int(possible_exits[dest]))