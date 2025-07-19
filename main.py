# Example file showing a circle moving on screen

import pygame

class Empire:
    spaceships = 0
    spaceships_build_speed = 0


def main():
    print("Hello from cosmicidle!")
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

	# Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    	
    # Create a font object
    font = pygame.font.Font(None, 74)  # None for default font, 74 is the size
    	
    # Render the text
    text_surface = font.render('Spaceships: ', True, WHITE)  # True for anti-aliasing
	 
    dt = 0
    
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    my_empire = Empire()
    
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
    
        # Blit the text surface onto the main display surface
        screen.blit(text_surface, (100, 250))  # Coordinates (100, 250)
        spaceships_surface = font.render(f'{Empire.spaceships}', True, WHITE)
        screen.blit(spaceships_surface, (100, 350))
        # delta_surface = font.render(f'{dt}', True, WHITE)
        # screen.blit(delta_surface, (0, 0))
        
#        pygame.draw.circle(screen, "red", player_pos, 40)
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_w]:
            Empire.spaceships += 1
#        if keys[pygame.K_s]:
#            player_pos.y += 300 * dt
#        if keys[pygame.K_a]:
#            player_pos.x -= 300 * dt
#        if keys[pygame.K_d]:
#            player_pos.x += 300 * dt
    
        # flip() the display to put your work on screen
        pygame.display.flip()
    
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
    
    pygame.quit()


if __name__ == "__main__":
    main()
