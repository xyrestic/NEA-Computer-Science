# menu_screen.py
import pygame
import time

# initialize pygame
pygame.init()

def start_menu_screen():
    # set up display for the menu screen
    menu_screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu Screen")

    # Create a font object
    font = pygame.font.Font(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\fonts\ChrustyRock-ORLA.ttf", 200)  # Increase the font size to 200

    # Create a surface for the text
    text_surface = font.render("Menu Screen", True, (255, 255, 255))  # White color

    # Calculate the position for the text surface to center it
    text_rect = text_surface.get_rect(center=(menu_screen.get_width() / 2, menu_screen.get_height() / 2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Blit the text surface onto the menu screen
        menu_screen.blit(text_surface, text_rect)

        pygame.display.flip()


# set up display
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Maths Pursuit")

# Load the background image
background = pygame.image.load(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\loading_screen.png")

font = pygame.font.Font(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\fonts\Abela Sweety.ttf", 64)  # Increase the font size to 64
running = True
count = 0

while running:
    # Blit the background image onto the screen
    screen.blit(background, (0, 0))

    count += 1
    if count <= 20:
        loading = "." * round(count%4)
        time.sleep(0.2)
        # Change the color over time
        color = ((count * 10) % 256, (count * 20) % 256, (count * 30) % 256)
        loading_surface = font.render(f"Loading {loading}", 0, color)
        # Calculate the position for the loading surface to center it horizontally and position it higher
        loading_rect = loading_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() - 100))
        screen.blit(loading_surface, loading_rect)

        # Draw the loading bar
        bar_width = screen.get_width() * 0.6  # 60% of the screen's width
        bar_height = 30
        bar_x = (screen.get_width() - bar_width) / 2
        bar_y = loading_rect.bottom + 20  # 20 pixels below the loading text
        border_width = 10  # Width of the border
        progress = count / 20  # Progress goes from 0 to 1

        # Draw the border of the loading bar
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(bar_x - border_width, bar_y - border_width, bar_width + 2 * border_width, bar_height + 2 * border_width), border_radius=15)
        # Draw the progress of the loading bar
        pygame.draw.rect(screen, color, pygame.Rect(bar_x, bar_y, bar_width * progress, bar_height), border_radius=10)

    elif count == 21:  # Add a delay after the loading bar is full
        time.sleep(2)  # Delay for 2 seconds
        start_menu_screen()  # Start the menu screen
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
