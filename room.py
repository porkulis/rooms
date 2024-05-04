import random
import sys
def roll(min, max):
    result = random.randint(min, max)
    return result

class Room:
    def __init__ (self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def set_exits(self, exits):
        self.exits = exits

    def describe_room(self):
        print(self.description)
    
    def list_exits(self):
        numered_exits = {}
        for key, value in self.exits.items():
            if value:
                numered_exits[key] = value
        possible_exits = []
        for key, value in numered_exits.items():
            if value:
                possible_exits.append(value)
        print("\nWyjścia: ")
        #print(possible_exits)
        i = 1
        #odp = ("a", "b", "c", "d")
        for ex in possible_exits:
            print(f"{i}. {getattr(__import__(__name__), ex).name}")
            i += 1
        return possible_exits




room_1 = Room("Komnata z głazem", "W komnacie znajduje się głaz.")
room_1.set_exits({"w": None, "e": "room_2"})

room_2 = Room("Komnata z fontanną", "W komnacie znajduje się fontanna krwi.")
room_2.set_exits({"w": "room_1", "e": "room_3"})

room_3 = Room("Komnata z dziurą", "W tej komnacie znajduje się dziura.")
room_3.set_exits({"w": "room_2", "e": "room_4"})

room_4 = Room("Komnata Skarbów", "W komnacie znajduje się skarbiec.")
room_4.set_exits({"w": None, "e": "room_3"})

room_5 = Room("Komnata 4", "Znajdujesz się w kryształowym więzieniu bez wyjść.")
room_5.set_exits({"w": None, "e": None})


def enter_room(room):
        current_room = room
        print(f"\nWchodzisz do: {current_room.name}")
        current_room.describe_room()
        possible_exits = current_room.list_exits()
        if current_room == room_3:
            answer = input("Chcesz wskoczyć do dziury?")
            if answer == "tak":
                print("GAME OVER")
                sys.exit()
        try:
            answer = int(input("Wybierz wyjscie: "))
            destination = possible_exits[answer - 1]
        except (ValueError, IndexError):
            print("Nieprawidłowy numer odpowiedzi.")
        next_room = getattr(__import__(__name__), destination)
        print(next_room.name)
        enter_room(next_room)

current_room = room_1
enter_room(current_room)









