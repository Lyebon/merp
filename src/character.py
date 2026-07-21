

class Character():
    def __init__(self):
        self.char: Stats = None

    def char_create(self) -> Stats:
        new_stats = {}
        self.char = Stats.to_dict(new_stats)
