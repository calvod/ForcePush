# Import a library of functions called 'pygame'
import pygame
from getNextScore import *
# Initialize the game engine
pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
currentScore = 0
PI = 3.141592653
# Set the width and height of the screen
size = (800, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pack Bonanza")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # Draw on the screen a line from (0,0) to (100,100)
    # 5 pixels wide.
    pygame.draw.line(screen, RED, [10, 10], [10+currentScore, 10], 5)
  
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
 
    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    scoreString = str(currentScore)
    text = font.render('Current Score: '+scoreString, True, BLACK)
 
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

    # wait for them to pack out another
    currentScore = currentScore + lookAtScreen()
# Be IDLE friendly
pygame.quit()
