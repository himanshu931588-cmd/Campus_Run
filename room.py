class Room:
    def __init__(self, name, width=1, height=1, walls=None, room_type=None):
        self.name = name
        self.width = width
        self.height = height
        self.walls = set(walls or [])
        self.room_type = room_type
        self.exits = {}
        self.interactions = {}

    def is_walkable(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.walls

    def connect(self, direction, destination, destination_x=0, destination_y=0):
        self.exits[direction.upper()] = (destination, destination_x, destination_y)

    def get_exit(self, direction):
        return self.exits.get(direction.upper())

    def add_interaction(self, x, y, target):
        self.interactions[(x, y)] = target

    def get_interaction(self, x, y):
        return self.interactions.get((x, y))

    def is_classroom(self):
        return self.room_type == "classroom" or self.name.casefold() == "classroom 404"