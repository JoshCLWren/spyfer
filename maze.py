

class Maze:
    """The maze class."""
    def __init__(self):
        """Initialize the maze."""
        self.M = 10
        self.N = 8
        self.maze = [ 1,1,1,1,1,1,1,1,1,1,
                      1,0,0,0,0,0,0,0,0,1,
                      1,0,0,0,0,0,0,0,0,1,
                      1,0,1,1,1,1,1,1,0,1,
                      1,0,1,0,0,0,0,0,0,1,
                      1,0,1,0,1,1,1,1,0,1,
                      1,0,0,0,0,0,0,0,0,1,
                      1,1,1,1,1,1,1,1,1,1,]

    def draw(self, display_surf, image_surf):
        """Draw the maze on the display surface."""
        bx = 0
        by = 0
        for _ in range(self.M * self.N):
            if self.maze[bx + (by * self.M)] == 1:
                display_surf.blit(image_surf, (bx * 44, by * 44))

            bx = bx + 1
            if bx > self.M - 1:
                bx = 0
                by = by + 1