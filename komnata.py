import random
import sys

class Komnata:
    def __init__ (self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def dodaj_wyjscie(self, direction, next_room):
        self.exits[direction] = next_room

komnaty = []

def create_description():
    x = ["stary", "zniszczony", "zmurszały", "lśniący"]
    a = ["kamienny", "marmurowy", "wapienny", "granitowy"]
    b = ["katafalk", "sarkofag", "posąg"]
    description = f"Znajduje się tu {random.choice(x)} {random.choice(a)} {random.choice(b)}"
    return description


def create_room():
    komnata = Komnata(f"Komnata {len(komnaty)+1}", f"{create_description()}.")
    komnaty.append(komnata)
    # name = f"room_{len(komnaty)+1}" #ustawienie poczatkowej nazwy instancji
    # setattr(komnata, "name", name)  # ustawienie dynamicznej nazwy instancji
    print(f"Tworzę komnatę o nazwie: {komnata.name}")

def change_room(room):
    current_room = komnaty[room-1]
    print(f"Wchodzisz do [{current_room.name}]. {current_room.description}")
    return current_room

for n in range(8):
    create_room()

i = 0
for n in range(len(komnaty)):
    print(f"{komnaty[i].name}: {komnaty[i].description}")
    i += 1

i = 1
for n in range(len(komnaty)):
    change_room(i)
    i += 1

def players_move():
    a = int(input(f"Dokąd chcesz iść? "))
    if a not in range(1,len(komnaty)+1):
        print("GAME OVER")
        sys.exit()
    current_room = change_room(a)
    return current_room

while True:
    current_room = players_move()
    print(f"{current_room.name}: {current_room.description}")




