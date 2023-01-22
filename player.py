class Player:
    """Player class for the game"""
    x = 10
    y = 10
    speed = 1

    def move_right(self):
        self.x = self.x + self.speed

    def move_left(self):
        self.x = self.x - self.speed

    def move_up(self):
        self.y = self.y - self.speed

    def move_down(self):
        self.y = self.y + self.speed