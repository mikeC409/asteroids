# Using code from the open-source pygame library
import pygame
import constants

def main():
    # initialize pygame
    pygame.init()

    # set screen width and heigh from our constants
    screen_width = constants.SCREEN_WIDTH
    screen_height = constants.SCREEN_HEIGHT

    # set up the display
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Asteroids")

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # set display black
        screen.fill((0, 0, 0))

        # refresh screen
        pygame.display.flip()
                


    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()