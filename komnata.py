import random
import sys

class Komnata:
    def __init__ (self, name, description):
        self.name = name
        self.description = description
        self.exits = {"północ": None, "wschód": None, "południe": None, "zachód": None}

    def dodaj_wyjscie(self, direction, next_room):
        self.exits[direction] = next_room

exits = {"północ": None, "wschód": None, "południe": None, "zachód": None}

komnaty = []

def create_description():
    x = ["stary", "zniszczony", "zmurszały", "lśniący"]
    a = ["kamienny", "marmurowy", "wapienny", "granitowy"]
    b = ["katafalk", "sarkofag", "posąg", "tron", "stół"]
    description = f"Znajduje się tu {random.choice(x)} {random.choice(a)} {random.choice(b)}"
    return description


def create_room():
    number_of_exits = random.randint(1,3)
    print(number_of_exits)
    komnata = Komnata(f"Komnata {len(komnaty)}", f"{create_description()}.")
    komnaty.append(komnata)
    # name = f"room_{len(komnaty)+1}" #ustawienie poczatkowej nazwy instancji
    # setattr(komnata, "name", name)  # ustawienie dynamicznej nazwy instancji
    print(f"Tworzę komnatę o nazwie: {komnata.name}")

def change_room(room):
    #previous_room = current_room
    current_room = komnaty[room]
    print(f"Wchodzisz do [{current_room.name}]. {current_room.description}")
    print(f"  Wyjścia: {current_room.exits}")
    return current_room

komnata = Komnata(f"Komnata 0", f"Komnata początkowa")
komnaty.append(komnata)
print(f"Tworzę komnatę o nazwie: {komnata.name}")

current_room = komnata

for n in range(3):
    create_room()

komnaty[0].exits["północ"] = komnaty[1].name #zmiana wyjścia z komnaty początkowej z "None" na komnata 1
komnaty[1].exits["południe"] = komnaty[0].name #zmiana wyjścia z komnaty 1 z "None" na komnata początkową

i = 0
for n in range(len(komnaty)):
    print(f"{komnaty[i].name}: {komnaty[i].description}")
    print(f"  Wyścia: {komnaty[i].exits}\n")
    i += 1

# i = 0
# for n in range(len(komnaty)):
#     change_room(i)
#     i += 1

def players_move():
    a = int(input(f"Dokąd chcesz iść? "))
    if a not in range(0,len(komnaty)):
        print("GAME OVER")
        sys.exit()
    current_room = change_room(a)
    return current_room


print(f"Znajdujesz się w [{current_room.name}]. {current_room.description}")
print(f"  Wyjścia: {current_room.exits}")
while True:
    current_room = players_move()
    #print(f"{current_room.name}: {current_room.description}") #test na to czy current room to ta sama do ktorej weszlismy




