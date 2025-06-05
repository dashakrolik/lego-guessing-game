# model.py

class LegoSet:
    def __init__(self, name, year, piece_count, theme):
        self.name = name
        self.year = year
        self.piece_count = piece_count
        self.theme = theme

    def summary(self):
        return f"{self.name} ({self.year}) - {self.piece_count} pieces - Theme: {self.theme}"

# Create an instance (object) of LegoSet
my_set = LegoSet("X-Wing Starfighter", 2020, 752, "Star Wars")

# Call the method and print the result
print(my_set.summary())