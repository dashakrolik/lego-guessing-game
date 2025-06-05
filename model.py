from typing import Optional

class LegoSet:
    def __init__(self, name: str, year: int, piece_count: int, theme: str, image_url: Optional[str] = None):
        self.name: str = name
        self.year: int = year
        self.piece_count: int = piece_count
        self.theme: str = theme
        self.image_url: Optional[str] = image_url  # ← this line was missing

    def image(self) -> str:
        if self.image_url:
            return "Image available"
        return "Image not available"

    def summary(self) -> str:
        return f"{self.name} ({self.year}) - {self.piece_count} pieces - Theme: {self.theme}. {self.image()}"
