from settings import *
from world import *


class Main:
    def __init__(self):
        # setup
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), vsync=1)
        pygame.display.set_caption('3 DOF Flight Controller')

    def main_loop(self):
        world = World()
        world.world_loop()

if __name__ == '__main__':
    main = Main()
    main.main_loop()
