class TodoItem:
    def __init__(self, title, priority=1, is_completed=False):
        self.title = title
        self.priority = priority
        self.is_completed = is_completed

    def __str__(self):
        return f"{self.title}, priority {self.priority}" + (
            "" if not self.is_completed else ", done")

    def __repr__(self):
        return f"TodoItem({self.title!r}, {self.priority!r}, {self.is_completed!r})"
