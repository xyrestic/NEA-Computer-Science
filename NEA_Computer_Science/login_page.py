import pygame
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\users.db")

# Create a cursor
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username text, password text)''')

# Commit the changes
conn.commit()

def sign_up(username, password):
    # Check if a user with the given username already exists
    c.execute('SELECT * FROM users WHERE username=?', (username,))
    if c.fetchone() is not None:
        return 'Username taken'
    # Insert a row of data
    c.execute("INSERT INTO users VALUES (?,?)", (username, password))
    # Save (commit) the changes
    conn.commit()
    return 'Sign up successful!'

def login(username, password):
    # Retrieve data
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    return c.fetchone() is not None


pygame.init()

win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Login Page")
font = pygame.font.Font(None, 32)
username_rect = pygame.Rect(540, 280, 200, 32)  # Modified location for username
password_rect = pygame.Rect(540, 320, 200, 32)  # Modified location for password
login_rect = pygame.Rect(590, 360, 100, 32)  # Modified location for login
signup_rect = pygame.Rect(590, 400, 100, 32)  # New location for signup
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color_username = color_inactive
color_password = color_inactive
active_username = False
active_password = False
username = 'Username'
password = 'Password'
done = False
message = ''

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:

            if username_rect.collidepoint(event.pos):
                active_username = True
                active_password = False
                color_username = color_active
                color_password = color_inactive
                if username == 'Username':
                    username = ''  # Clear the username text

            elif password_rect.collidepoint(event.pos):
                active_password = True
                active_username = False
                color_password = color_active
                color_username = color_inactive
                if password == 'Password':
                    password = ''  # Clear the password text

            # Check if the login button is clicked
            elif login_rect.collidepoint(event.pos):
                if username == 'Username' or password == 'Password':
                    message = 'Please enter a valid username or password.'
                elif login(username, password):
                    import menu_screen
                    done = True  # Close the login window
                else:
                    message = 'Please sign up first.'

        	# Check if the signup button is clicked
            elif signup_rect.collidepoint(event.pos):
        	    if username == 'Username' or password == 'Password':
        	        message = 'Please enter a valid username or password.'
        	    else:
        	        message = sign_up(username, password)

            else:
                active_username = False
                active_password = False
                color_username = color_inactive
                color_password = color_inactive
                if username == '':
                    username = 'Username'
                if password == '':
                    password = 'Password'

        if event.type == pygame.KEYDOWN:
            if active_username:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode
            if active_password:
                if event.key == pygame.K_BACKSPACE:
                    password = password[:-1]
                else:
                    password += event.unicode
            if event.key == pygame.K_RETURN:
                print(username, password)
                username = 'Username'
                password = 'Password'

    win.fill((30, 30, 30))
    username_surface = font.render(username, True, color_username)
    width = max(200, username_surface.get_width() + 10)
    username_rect.w = width
    win.blit(username_surface, (username_rect.x + 5, username_rect.y + 5))
    pygame.draw.rect(win, color_username, username_rect, 2)
    if password != 'Password':
        password_surface = font.render('*' * len(password), True, color_password)
    else:
        password_surface = font.render(password, True, color_password)
    width = max(200, password_surface.get_width() + 10)
    password_rect.w = width
    win.blit(password_surface, (password_rect.x + 5, password_rect.y + 5))
    pygame.draw.rect(win, color_password, password_rect, 2)
    login_surface = font.render('LOGIN', True, color_inactive)
    win.blit(login_surface, (login_rect.x + 5, login_rect.y + 5))
    pygame.draw.rect(win, color_inactive, login_rect, 2)
    signup_surface = font.render('SIGN UP', True, color_inactive)
    win.blit(signup_surface, (signup_rect.x + 5, signup_rect.y + 5))
    pygame.draw.rect(win, color_inactive, signup_rect, 2)
    # Create a new surface for the message
    if message in ['Sign up successful!', 'Login successful!']:
        message_color = (0, 255, 0)  # Green color
    else:
        message_color = (255, 0, 0)  # Red color
    message_surface = font.render(message, True, message_color)

    # Calculate the position for the message surface to center it horizontally and position it just below the sign up button
    message_rect = message_surface.get_rect(center=(win.get_width() / 2, signup_rect.y + signup_rect.height + 20))

    # Blit the message surface onto the main window
    win.blit(message_surface, message_rect)

    pygame.display.flip()

conn.close()
pygame.quit()