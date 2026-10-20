from settings import *
from controller import *


class


class Drone(pygame.sprite.Sprite):
    def __init__(self, groups, pos, target_pos):
        # setup
        super().__init__(groups)
        self.image = self.create_image()
        self.rect = self.image.get_frect(center=pos)

        # scalars
        self.mass = 10

        # vectors
        self.target_pos = pygame.math.Vector2(target_pos)
        self.pos = pygame.math.Vector2(pos)
        self.thrust = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()

        # targeting
        self.error = pygame.math.Vector2()
        self.target_velocity = pygame.math.Vector2()

        # saturation limits
        self.thrust = 10000

        # controllers
        self.velocity_controller = Controller(0,0,0,None)
        self.thrust_controller = Controller(0.1, 0.1, 0.1, self.thrust)

    def create_image(self):
        surf = pygame.Surface((100, 20), pygame.SRCALPHA)
        surf.fill((150,150,150))

        thruster_surf = pygame.Surface((20, 20), pygame.SRCALPHA)
        thruster_surf.fill((200, 50, 50))

        surf.blit(thruster_surf, (0, 0))
        surf.blit(thruster_surf, (80, 0))

        return surf

    def update_motion(self, dt):
        self.acceleration = (self.thrust/self.mass) + GRAVITY
        self.velocity += self.acceleration * dt
        self.pos += self.velocity * dt

        self.rect.center = self.pos

    def calculate_error(self):
        self.error = self.target_pos-self.pos

    def get_thrust(self, dt):
        self.target_velocity = self.velocity_controller.calculate_actuating_signal(self.error, dt)
        self.thrust = self.thrust_controller.calculate_actuating_signal(self.target_velocity - self.velocity, dt)

    def update(self, dt):
        self.update_motion(dt)