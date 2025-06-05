class LegoSet:
    def __init__(self, name, year, piece_count, theme):
        self.name = name
        self.year = year
        self.piece_count = piece_count
        self.theme = theme

    def summary(self):
        return f"{self.name} ({self.year}) - {self.piece_count} pieces - Theme: {self.theme}"
