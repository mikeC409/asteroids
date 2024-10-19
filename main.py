# Using code from the open-source pygame library
import pygame
import constants
from player import Player

def main():
    # initialize pygame
    pygame.init()

    # set screen width and heigh from our constants
    screen_width = constants.SCREEN_WIDTH
    screen_height = constants.SCREEN_HEIGHT

    # set up the display
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Asteroids")

    # set up a Clock object to help restrict our game to 60fps
    clock = pygame.time.Clock()
    dt = 0

    # instantiate the player object at the center of the screen
    player = Player(screen_width / 2, screen_height / 2)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # set display black
        screen.fill((0, 0, 0))

        # update the player
        player.update(dt)

        # draw the player
        player.draw(screen)

        # refresh screen
        pygame.display.flip()

        # Limit the frame rate to 60fps
        dt = clock.tick(60) / 1000.0 # convert milliseconds to seconds
                


    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()