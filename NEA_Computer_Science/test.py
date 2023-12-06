import pygame

# Initialize Pygame
pygame.init()

# Set up some constants
NUM_FRAMES = 3
WIDTH, HEIGHT = 1280, 720
FPS = 5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the frames of the GIF, ‘frame0.png’, ‘frame1.png’, ‘frame2.png’
frames = [pygame.image.load(f'C:\\Users\\Dylan\\OneDrive\\Documents\\NEA_Computer_Science\\images\\testGIF{i}.png') for i in range(NUM_FRAMES)]

# Game loop
running = True
frame_num = 0
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the current frame
    screen.blit(frames[frame_num], (0, 0))

    # Move to the next frame
    frame_num = (frame_num + 1) % NUM_FRAMES

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(FPS)

pygame.quit()