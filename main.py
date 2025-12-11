import pygame

from logger import log_state

from constants import SCREEN_WIDTH, SCREEN_HEIGHT



def main():
    
    pygame.init()

    clock = pygame.time.Clock()
    
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running = True
    
    while running:

        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        
        #print(dt)

    

if __name__ == "__main__":
    main()
