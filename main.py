from item import Item, create_timetable
from player import Player


def make_demo_player():
    id_card = Item("ID Card")
    timetable = create_timetable()
    return Player(inventory=[id_card, timetable])


def show_ui(player):
    print("+------------------------------------------------+")
    print("|                 CAMPUS RUN                    |")
    print("+------------------------------------------------+")
    print("| OBJECTIVE                                      |")
    print("| Reach Classroom 404 before class begins.       |")
    print("+------------------------------------------------+")
    print("| CAMPUS MAP                                     |")
    print("|                                                |")
    print("| [MAIN GATE] -> [CORRIDOR] -> [STAIRS]         |")
    print("|                              |                 |")
    print("|                         [FLOOR 2]              |")
    print("|                              |                 |")
    print("|                         [FLOOR 3]              |")
    print("|                              |                 |")
    print("|                    [CLASSROOM 404]             |")
    print("+------------------------------------------------+")
    print(f"| LOCATION: {player.current_room.name:<35}|")
    print(f"| TIME:     {player.get_current_time():<35}|")
    print(f"| TIME LEFT: {player.get_time_left()} seconds{' ' * 23}|")
    print("+------------------------------------------------+")
    print("| INVENTORY                                      |")
    for item in player.inventory:
        print(f"| - {item.name:<43}|")
    print("+------------------------------------------------+")
    print("| CONTROLS                                       |")
    print("| W A S D  Move                                  |")
    print("| E        Interact                              |")
    print("| I        Open inventory                        |")
    print("| Q        Quit                                  |")
    print("+------------------------------------------------+")


if __name__ == "__main__":
    show_ui(make_demo_player())