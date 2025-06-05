class LegoSet:
    def __init__(self, name: str, year: int, piece_count: int, theme: str):
        self.name: str = name
        self.year: int = year
        self.piece_count: int = piece_count
        self.theme: str = theme

    def summary(self) -> str:
        return f"{self.name} ({self.year}) - {self.piece_count} pieces - Theme: {self.theme}"
