from room import Room


START_TIME = 9 * 60 * 60 + 25 * 60
SECURITY_TIME = 2 * 60
CLASS_TIME = 9 * 60 * 60 + 30 * 60
MOVE_TIME = 5
INTERACTION_TIME = 10
STAIR_TIME = 10
FRIEND_TIME = 20
CANTEEN_TIME = 20


class Player:
    DIRECTIONS = {
        "W": (0, -1),
        "A": (-1, 0),
        "S": (0, 1),
        "D": (1, 0),
    }

    def __init__(self, name="Student", current_room=None, inventory=None, time=None, x=0, y=0):
        self.name = name
        if current_room is None:
            self.current_room = Room("Main Gate")
        else:
            self.current_room = current_room

        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory.copy()

        if time is None:
            self.time = START_TIME + SECURITY_TIME
        else:
            self.time = time
        self.x = x
        self.y = y

    def move(self, direction):
        direction = str(direction).upper()
        if direction not in self.DIRECTIONS:
            return "Invalid direction. Use W, A, S, or D."

        offset_x, offset_y = self.DIRECTIONS[direction]
        next_x = self.x + offset_x
        next_y = self.y + offset_y

        if self.current_room.is_walkable(next_x, next_y):
            self.x = next_x
            self.y = next_y
            self.advance_time(MOVE_TIME)
            return f"You move to {self.current_room.name}."

        exit_data = self.current_room.get_exit(direction)
        if exit_data is None:
            return 'You cannot move there. That is a wall.'

        destination, destination_x, destination_y = exit_data
        self.current_room = destination
        self.x = destination_x
        self.y = destination_y
        if destination.name.lower() == "stairs":
            self.advance_time(STAIR_TIME)
        else:
            self.advance_time(MOVE_TIME)
        return f"You enter {self.current_room.name}."

    def interact(self, target=None):
        if target is None:
            target = self.current_room.get_interaction(self.x, self.y)
            if target is None:
                return "There is nothing to interact with here."

        self.advance_time(INTERACTION_TIME)
        if hasattr(target, "interact"):
            return target.interact(self)
        return str(target)

    def pick_item(self, item):
        if item is None or not hasattr(item, "name"):
            return "Invalid item."
        if self.has_item(item.name):
            return f"You already have the {item.name}."
        self.inventory.append(item)
        return f"You picked up the {item.name}."

    def remove_item(self, item):
        index = self._item_index(item)
        if index is None:
            return "That item is not in your inventory."
        removed = self.inventory.pop(index)
        return f"You removed the {removed.name}."

    def show_inventory(self):
        lines = ["================================", "INVENTORY", "================================"]
        if not self.inventory:
            lines.append("Empty")
        else:
            number = 1
            for item in self.inventory:
                lines.append(f"{number}. {item.name}")
                number += 1
        lines.append("================================")
        return "\n".join(lines)

    def has_item(self, item):
        return self._item_index(item) is not None

    def use_item(self, item):
        index = self._item_index(item)
        if index is None:
            return "That item is not in your inventory."
        self.advance_time(INTERACTION_TIME)
        return self.inventory[index].use(self)

    def advance_time(self, seconds):
        if not isinstance(seconds, (int, float)) or seconds < 0:
            raise ValueError("seconds must be a non-negative number")
        self.time += seconds

    def get_current_time(self):
        total_seconds = int(self.time) % (24 * 60 * 60)
        hours, remainder = divmod(total_seconds, 60 * 60)
        minutes = remainder // 60
        suffix = "AM" if hours < 12 else "PM"
        display_hour = hours % 12 or 12
        return f"{display_hour}:{minutes:02d} {suffix}"

    def get_time_left(self):
        time_left = int(CLASS_TIME - self.time)
        if time_left < 0:
            return 0
        return time_left

    def is_late(self):
        return self.time >= CLASS_TIME

    def get_arrival_band(self):
        elapsed = self.time - CLASS_TIME
        if elapsed < 0:
            return "before_9:30"
        if elapsed <= 2 * 60:
            return "9:30-9:32"
        if elapsed <= 5 * 60:
            return "9:33-9:35"
        return "after_9:35"

    def is_in_classroom(self):
        return self.current_room.is_classroom()

    def _item_index(self, item):
        if hasattr(item, "name"):
            item_name = item.name
        else:
            item_name = item

        for index, inventory_item in enumerate(self.inventory):
            if inventory_item is item or inventory_item.name == item_name:
                return index
        return None