from item import Item, create_timetable
from player import Player
from room import Room


def make_demo_player():
    id_card = Item("ID Card")
    timetable = create_timetable()
    main_gate = Room("Main Gate")
    corridor = Room("Main Corridor")
    stairs = Room("Stairs")
    floor_2 = Room("Floor 2")
    floor_3 = Room("Floor 3")
    floor_4 = Room("Floor 4")
    classroom = Room("Classroom 404", room_type="classroom")

    main_gate.connect("D", corridor)
    corridor.connect("D", stairs)
    stairs.connect("D", floor_2)
    floor_2.connect("D", floor_3)
    floor_3.connect("D", floor_4)
    floor_4.connect("D", classroom)

    classroom.add_interaction(0, 0, "You open the door to Classroom 404.")
    return Player(current_room=main_gate, inventory=[id_card, timetable])


def show_ui(player, message=""):
    print("\n" * 2)
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
    print("|                         [FLOOR 4]              |")
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
    if message:
        print(f"\n{message}")


def run_game():
    player = make_demo_player()
    message = "Security finished. Get to class!"

    while True:
        show_ui(player, message)
        command = input("\nCommand: ").strip().upper()

        if command == "Q":
            print("You leave campus. Class will have to wait.")
            break
        if command == "I":
            message = player.show_inventory()
            continue
        if command == "E":
            message = player.interact()
            continue
        if command in player.DIRECTIONS:
            message = player.move(command)
            if player.is_in_classroom():
                message = player.interact()
                show_ui(player, message)
                print(f"\nArrival result: {player.get_arrival_band()}")
                break
            continue

        message = "Invalid command. Use W, A, S, D, E, I, or Q."


if __name__ == "__main__":
    run_game()