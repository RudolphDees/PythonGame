import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Basic Pygame Window")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Game variables
circle_x, circle_y = WIDTH // 2, HEIGHT // 2
circle_radius = 30
circle_speed = 5
circle_color = RED
paused = False

# Clock to control frame rate
clock = pygame.time.Clock()

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_pause_menu():
    menu_width, menu_height = 300, 200
    menu_x, menu_y = (WIDTH - menu_width) // 2, (HEIGHT - menu_height) // 2
    pygame.draw.rect(screen, GRAY, (menu_x, menu_y, menu_width, menu_height))
    pygame.draw.rect(screen, BLACK, (menu_x, menu_y, menu_width, menu_height), 3)
    
    font = pygame.font.Font(None, 36)
    continue_text = font.render("Continue", True, BLACK)
    quit_text = font.render("Quit", True, BLACK)
    
    continue_button = pygame.Rect(menu_x + 50, menu_y + 50, 200, 50)
    quit_button = pygame.Rect(menu_x + 50, menu_y + 120, 200, 50)
    
    pygame.draw.rect(screen, WHITE, continue_button)
    pygame.draw.rect(screen, WHITE, quit_button)
    pygame.draw.rect(screen, BLACK, continue_button, 2)
    pygame.draw.rect(screen, BLACK, quit_button, 2)
    
    screen.blit(continue_text, (menu_x + 110, menu_y + 65))
    screen.blit(quit_text, (menu_x + 130, menu_y + 135))
    
    return continue_button, quit_button

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            paused = not paused
        elif event.type == pygame.MOUSEBUTTONDOWN and paused:
            mouse_x, mouse_y = event.pos
            continue_button, quit_button = draw_pause_menu()
            if continue_button.collidepoint(mouse_x, mouse_y):
                paused = False
            elif quit_button.collidepoint(mouse_x, mouse_y):
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if (mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2 <= circle_radius ** 2:
                circle_color = random_color()
    
    if paused:
        screen.fill(WHITE)
        draw_pause_menu()
    else:
        # Move circle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            circle_x -= circle_speed
        if keys[pygame.K_d]:
            circle_x += circle_speed
        if keys[pygame.K_w]:
            circle_y -= circle_speed
        if keys[pygame.K_s]:
            circle_y += circle_speed
        
        # Draw everything
        screen.fill(WHITE)
        pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
    
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
