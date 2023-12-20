import pygame, time, sys ,subprocess, os

# initialize pygame
pygame.init()

main_font = pygame.font.Font(None, 32)

class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("Button Press!")

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "white")

def start_menu_screen():
    # set up display for the menu screen
    menu_screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu Screen")

    # Load the frames of the GIF
    FPS = 3
    NUM_FRAMES = 3
    frames = [pygame.image.load(fr"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\bg{i}.png") for i in range(NUM_FRAMES)]
    frame_num = 0

    # Create a font object for the title
    title_font = pygame.font.Font(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\fonts\Hamston.ttf", 100)  # Decrease the font size to 100

    # Create a surface for the title
    title_text = "MATHS PURSUIT"
    title_surface = title_font.render(title_text, True, (242, 239, 233))  # White color

    # Calculate the position for the title surface to center it horizontally and position it at the top
    title_rect = title_surface.get_rect(center=(menu_screen.get_width() / 2 + 140, 50))  # Move the title 50 pixels to the right

    # Create an outline for the title
    outline_color = (86, 78, 88)  # Black color
    outline_width = 4  # Increase the width of the outline
    for x in range(-outline_width, outline_width+1):
        for y in range(-outline_width, outline_width+1):
            if x != 0 or y != 0:  # Avoid the center
                outline_surface = title_font.render(title_text, True, outline_color)
                menu_screen.blit(outline_surface, (title_rect.x + x, title_rect.y + y))

    # Blit the title surface onto the menu screen
    menu_screen.blit(title_surface, title_rect)

    # Create the buttons
    button_height = (menu_screen.get_height() - title_rect.bottom - 100) / 4  # Leave some space for the title and margins
    button_width = menu_screen.get_width() / 4
    button_font = pygame.font.Font(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\fonts\PositionsByArixbored-Regular .otf", 32)
    button_names = ["Play", "Level Select", "Characters", "Quit"]
    gap = 50  # Define the size of the gap
    buttons = [Button(pygame.Surface((button_width, button_height)), gap + menu_screen.get_width() / 8, title_rect.bottom + 50 + i * (button_height + 20), name) for i, name in enumerate(button_names)]

    # Change the color of the buttons and the text
    for button in buttons:
        button.image.fill((242, 239, 233))  # Fill the buttons with white color
        button.text = button_font.render(button.text_input, True, (0, 0, 0))  # Render the text in black color

    # Create the small button at the top right242, 239, 233
    small_button = Button(pygame.Surface((50, 50)), menu_screen.get_width() - 25, 25, "")
    small_button.image = pygame.image.load(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\settings_cog.png")
    small_button.image = pygame.transform.scale(small_button.image, (50, 50))  # Adjust the size as needed

    running = True
    while running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for a mouse click
                if event.button == 1:  # Check if the left mouse button was clicked
                    for button in buttons:
                        if button.rect.collidepoint(event.pos):  # Check if the button was clicked
                            if button.text_input == "Quit":
                                pygame.quit()
                                sys.exit()
                            elif button.text_input == "Play":
                                subprocess.Popen(["python", r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\play_button\play.py"])
                                pygame.display.quit()
                                pygame.quit()
                                os._exit(0)

        # Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Draw the current frame
        menu_screen.blit(frames[frame_num], (0, 0))

        # Blit the title outline and the title surface onto the menu screen
        for x in range(-outline_width, outline_width+1):
            for y in range(-outline_width, outline_width+1):
                if x != 0 or y != 0:  # Avoid the center
                    outline_surface = title_font.render(title_text, True, outline_color)
                    menu_screen.blit(outline_surface, (title_rect.x + x, title_rect.y + y))
        menu_screen.blit(title_surface, title_rect)

        # Move to the next frame
        frame_num = (frame_num + 1) % NUM_FRAMES

        # Update the buttons
        for button in buttons:
            button.update()
            # Change the color of the button's outline if the mouse is hovering over it
            if button.rect.collidepoint(mouse_pos):
                pygame.draw.rect(menu_screen, pygame.Color(144, 78, 85), button.rect, 5)
            else:
                pygame.draw.rect(menu_screen, pygame.Color(86, 78, 88), button.rect, 5)

        # Update the small button
        small_button.update()

        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(FPS)



# set up display
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Maths Pursuit")

# Load the background image
loading_image = pygame.image.load(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\loading_screen.png")

font = pygame.font.Font(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\fonts\Abela Sweety.ttf", 64)  # Increase the font size to 64
running = True
count = 0

while running:
    # Blit the background image onto the screen
    screen.blit(loading_image, (0, 0))

    count += 1
    if count <= 200:  # Increase the total count to slow down the loading
        loading = "." * round((count // 50) % 4)  # Adjust the loading text to match the slower loading
        time.sleep(0.01)  # Shorter delay for smoother loading
        # Change the color over time
        color = ((count // 2) % 256, (count // 4) % 256, (count // 8) % 256)
        loading_surface = font.render(f"Loading {loading}", 0, color)
        # Calculate the position for the loading surface to center it horizontally and position it higher
        loading_rect = loading_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() - 200))  # Move the loading text 100 pixels up
        screen.blit(loading_surface, loading_rect)

        # Draw the loading bar
        bar_width = screen.get_width() * 0.6  # 60% of the screen's width
        bar_height = 30
        bar_x = (screen.get_width() - bar_width) / 2
        bar_y = loading_rect.bottom + 20  # 20 pixels below the loading text
        border_width = 10  # Width of the border
        progress = count / 200  # Progress goes from 0 to 1

        # Draw the border of the loading bar
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(bar_x - border_width, bar_y - border_width, bar_width + 2 * border_width, bar_height + 2 * border_width), border_radius=15)
        # Draw the progress of the loading bar
        pygame.draw.rect(screen, color, pygame.Rect(bar_x, bar_y, bar_width * progress, bar_height), border_radius=10)  # Move the loading bar 50 pixels up

    elif count == 201:  # Add a pause after the loading bar is full
        time.sleep(2)  # Pause for 2 seconds
        count += 1  # Increase the count to prevent the pause from repeating
    else:
        start_menu_screen()  # Start the menu screen
        running = False  # Close the loading window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()