import pygame
import sys

from logger import log_state, log_event

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    
    pygame.init()

    clock = pygame.time.Clock()
    
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()

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

        
        for obj in updatable:
            obj.update(dt)


        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            for shot in shots:
            
                if asteroid.collides_with(shot):
                   log_event("asteroid_hit")
                   shot.kill()
                   asteroid.split()


        pygame.display.flip()

        dt = clock.tick(60) / 1000
        
        #print(dt)

    

if __name__ == "__main__":
    main()
