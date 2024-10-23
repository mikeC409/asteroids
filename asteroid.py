import pygame
import random
import constants
from circleshape import CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # draw asteroid as a circle
        pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)),
                           self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # kill current asteroid
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        # generating a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector2 * 1.2
