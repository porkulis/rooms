import random
import sys

class Komnata:
    def __init__ (self, name, number, description):
        self.name = name
        self.number = number
        self.description = description
        self.exits = {"północ": None, "wschód": None, "południe": None, "zachód": None}

    def dodaj_wyjscie(self, direction, next_room):
        self.exits[direction] = next_room


komnaty = [] #stworzenie pustej listy do przechowywania komnat
possible_exits = []
visited_rooms = []

def create_name():
    x = ["ciemna", "obszerna", "ciasna"]
    a = ["kamienna", "wilgotna", "skalna", "solna"]
    b = ["komnata", "grota", "sala"]
    name = f"{random.choice(x)} {random.choice(a)} {random.choice(b)}"
    return name

def create_description():
    x = ["stary", "zniszczony", "zmurszały", "lśniący"]
    a = ["kamienny", "marmurowy", "wapienny", "granitowy"]
    b = ["katafalk", "sarkofag", "posąg", "tron", "stół"]
    description = f"Znajduje się tu {random.choice(x)} {random.choice(a)} {random.choice(b)}"
    return description


def create_room():
    # number_of_exits = random.randint(1,3)
    # print(f"number_of_exits: {number_of_exits}")
    komnata = Komnata(f"{create_name()}", len(komnaty), f"{create_description()}.")
    komnaty.append(komnata)
    # name = f"room_{len(komnaty)+1}" #ustawienie poczatkowej nazwy instancji
    # setattr(komnata, "name", name)  # ustawienie dynamicznej nazwy instancji
    #print(f"Tworzę komnatę o nazwie: {komnata.name}")

def change_room(room):
    #previous_room = current_room
    current_room = komnaty[room]
    possible_exits = []
    print(f"\nTwoim oczom ukazuje się {current_room.name}.\n \n{current_room.description}")
    if current_room.name not in visited_rooms:
        print("Jesteś tu po raz pierwszy.")
    else:
        print("Już tu byłeś.")
    if current_room.name not in visited_rooms:
        visited_rooms.append(current_room.name)
    #print(f"   Odwiedzone komnaty: {visited_rooms}")
    print("Możliwe wyjścia:")
    for key, value in current_room.exits.items():
        if value != None:
            print(f"   - {key}: {value.name}")
            possible_exits.append(value)
    return current_room


def players_move():
    a = int(input(f"Dokąd chcesz iść? "))
    if a not in range(0,len(komnaty)):
        print("GAME OVER")
        sys.exit()
    current_room = change_room(a)
    return current_room

def choose_direction():
    ans = 0
    while ans not in ["w","s","a","d","q"]:
        ans = input("\nWybierz wyjście (W-zachód, S-południe, A-zachód, D-wschód, Q-zakończ grę): ")
    if ans == "q":
        endgame = input("Czy na pewno chcesz zakończyć grę? (y/n): ")
        if endgame == "y":
            print("\nZrobisz mi herbkę? :)\n")
            sys.exit()
    elif ans == "w":
        dest = "północ"
    elif ans == "s":
        dest = "południe"
    elif ans == "a":
        dest = "zachód"
    elif ans == "d":
        dest = "wschód"
    return dest

#main##############################################

#Stworzenie pierwszej komnaty
komnata = Komnata(f"sala wejściowa", 0, f"Znajdują się tutaj potężne drewniane drzwi prowadzące na wschód.")
komnaty.append(komnata)
print(f"Tworzę komnatę o nazwie: {komnata.name}")

current_room = komnata #ustawienie początkowej lokacji gracza

#Stworzenie pozostałych komnat i ścieżek
z = 0
for n in range(100):
    create_room()
    komnaty[z].exits["wschód"] = komnaty[z+1] 
    komnaty[z+1].exits["zachód"] = komnaty[z]
    z += 1

print("\n---Lista stworzonych komnat i wyjść:")
i = 0
for n in range(len(komnaty)):
    print(f"{komnaty[i].name}: numer: {komnaty[i].number}, {komnaty[i].description}")
    print(f"  Wyścia: {komnaty[i].exits}")
    i += 1



# print("\n---Test chodzenia po komnatach")
# i = 0
# for n in range(len(komnaty)):
#     change_room(i)
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
    #print(kierunki)
    #print(possible_exits)

    dest = choose_direction()

    if dest not in directions:
        print(f"Na {dest} jest lita ściana.")
    elif dest in directions:
        print(f"\nRuszasz na {dest}.")
        current_room = change_room(int(possible_exits[dest]))





# print(f"Znajdujesz się w [{current_room.name}]. {current_room.description}")
# print(f"  Wyjścia: {current_room.exits}")
# while True:
#     current_room = players_move()
#     #print(f"{current_room.name}: {current_room.description}") #test na to czy current room to ta sama do ktorej weszlismy
