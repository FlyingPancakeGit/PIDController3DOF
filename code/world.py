from settings import *
from drone import *


class World:
    def __init__(self):
        # setup
        self.display_surface = pygame.display.get_surface()
        self.running = True
        self.clock = pygame.time.Clock()

        # groups
        self.drone_sprite_group = pygame.sprite.Group()

        # drone
        self.drone = Drone(self.drone_sprite_group, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), (50,50))

    def world_loop(self):
        while self.running:
            dt = self.clock.tick() / 1000

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.drone_sprite_group.update(dt)

            # draw
            self.display_surface.fill((50,50,50))
            self.drone_sprite_group.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()