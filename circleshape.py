import pygame

# Create base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def check_collision(self, other):
        # calculating distance between the two asteroids (CircleShape object)
        distance = self.position.distance_to(other.position)

        # check if distance is less than the sum of the radii
        return distance <= (self.radius + other.radius)