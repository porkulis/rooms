import random

class Komnata:
    def __init__ (self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def dodaj_wyjscie(self, direction, next_room):
        self.exits[direction] = next_room

komnaty = []
print(f"Liczba komnat: {len(komnaty)}")

def create_room():
    komnata = Komnata(f"Komnata_{len(komnaty)}", "Opis losowej komnaty")
    komnaty.append(komnata)
    # name = f"room_{len(komnaty)+1}" #ustawienie poczatkowej nazwy instancji
    # setattr(komnata, "name", name)  # ustawienie dynamicznej nazwy instancji
    print(f"Tworzę komnatę o nazwie: {komnata.name}")

create_room()

create_room()

create_room()

print(f"Liczba komnat: {len(komnaty)}")
print(f"Lista instancji komnat: {komnaty}")

i = 0
for n in range(len(komnaty)):
    print(f"{komnaty[i].name} {komnaty[i].description}")
    i += 1





