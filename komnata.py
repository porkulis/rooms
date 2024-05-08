import random
import sys


class Komnata:
    def __init__(self, name, number, description):
        self.name = name
        self.number = number
        self.description = description
        self.exits = {"północ": None, "wschód": None, "południe": None, "zachód": None}

    def dodaj_wyjscie(self, direction, next_room):
        self.exits[direction] = next_room


komnaty = []  #stworzenie pustej listy do przechowywania komnat
possible_exits = []
visited_rooms = []


def create_name():
    a = ["ciasna", "niewielka", "spora", "przestronna", "ogromna"]
    b = ["komnata", "grota", "sala"]
    name = f"{random.choice(a)} {random.choice(b)}"
    return name


def create_description():
    x = ["stary", "zniszczony", "zmurszały", "lśniący"]
    a = ["kamienny", "marmurowy", "wapienny", "granitowy"]
    b = ["katafalk", "sarkofag", "posąg", "tron", "stół"]
    i = random.randint(1, 3)
    if i == 1:
        description = "Jest tu zupełnie pusto"
    else:
        description = f"Znajduje się tu {random.choice(x)} {random.choice(a)} {random.choice(b)}"
    return description


def create_room():
    komnata = Komnata(f"{create_name()}", len(komnaty), f"{create_description()}.")
    komnaty.append(komnata)

def change_room(room):
    current_room = komnaty[room]

    possible_exits = []

    print("_____________________________________________________________")
    print(f"Twoim oczom ukazuje się {current_room.name.title()} (Komnata {current_room.number}).")
    print(f"{current_room.description}")

    if current_room not in visited_rooms:
        print("\nJesteś tu po raz pierwszy.")
    else:
        print("\nJuż tu byłeś.")
    if current_room not in visited_rooms:
        visited_rooms.append(current_room)

    print("\nMożliwe wyjścia:")
    numerator = 1
    for key, value in current_room.exits.items():
        if value != None:
            print(f" --> {numerator}. {key}: {value.name.title()} (Komnata {value.number})")
            numerator += 1
        else:
            print(f"     {numerator}. {key}: Brak")
            numerator += 1
    return current_room


def choose_direction():
    global dest
    ans = 0
    while ans not in ["1", "2", "3", "4"]:
        #print(f"\nWybór kierunku: 1, 2, 3, 4 lub Q by zakończyć grę.")
        ans = input("\nWybierz wyjście: ")
        if ans == "q":
            ans = input("Czy na pewno chcesz zakończyć grę? (y/n): ")
            if ans == "y":
                print("\nZrobisz mi herbkę? :)\n")
                sys.exit()
        elif ans == "1":
            dest = "północ"
        elif ans == "2":
            dest = "wschód"
        elif ans == "3":
            dest = "południe"
        elif ans == "4":
            dest = "zachód"
    return dest
