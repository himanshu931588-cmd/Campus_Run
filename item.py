class Item:
    def __init__(self, name, details="", usable=False, use_action=None):
        self.name = name
        self.details = details
        self.usable = usable
        self.use_action = use_action

    def use(self, player):
        if not self.usable:
            return f"You cannot use the {self.name}."
        if self.use_action is None:
            if self.details:
                return f"{self.name}: {self.details}"
            return f"You use the {self.name}."
        return self.use_action(player)

    def __str__(self):
        return self.name


def create_timetable():
    details = "Python Programming | Room 404 | Floor 4 | 9:30 AM"
    return Item("Timetable", details, usable=True)