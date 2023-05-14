import pygame
import sys
import os

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
pygame.font.init()
CIRCLE_TEXT_FONT = pygame.font.Font("/Users/ryanwisniewski/Documents/Inter/static/Inter-Regular.ttf", 20)
TITLE_FONT = pygame.font.Font("/Users/ryanwisniewski/Documents/Inter/static/Inter-Regular.ttf", 29)
INSTRUCTION_FONT = pygame.font.Font("/Users/ryanwisniewski/Documents/Inter/static/Inter-Regular.ttf", 15)

# Constants for game states
START = "start"
GAME = "game"
END = "end"

# Initialize game_state
game_state = START

# Other constants
FPS = 60

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reflective Exercise")
clock = pygame.time.Clock()

# Define the draw_start_screen function here
def draw_start_screen():
    screen.fill(WHITE)
    pygame.draw.rect(screen, WHITE, start_button_rect)  # Change menu_button_color to WHITE
    start_text_surface = menu_font.render("Start", True, BLACK)
    start_text_rect = start_text_surface.get_rect(center=start_button_rect.center)
    screen.blit(start_text_surface, start_text_rect)

# Define the draw_game_screen function here
def draw_game_screen():
    global opening_progress
    screen.fill(WHITE)

# Define the draw_end_screen function here
def draw_end_screen():
    # Add the code to draw the end screen here
    pass

menu_font = pygame.font.Font("/Users/ryanwisniewski/Documents/Inter/static/Inter-Regular.ttf", 30)
start_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if game_state == START:
                # Check if the mouse is over the start button and change the game state to 'game'
                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    game_state = GAME
            elif game_state == GAME:
                # Handle mouse click events for the main game
                pass
            elif game_state == END:
                # Handle mouse click events for the end screen
                pass

    # Game logic
    if game_state == START:
        draw_start_screen()
    elif game_state == GAME:
        draw_game_screen()
    elif game_state == END:
        draw_end_screen()

    pygame.display.flip()
    clock.tick(FPS)

    # Game logic
    if game_state == START:
        draw_start_screen()
    elif game_state == GAME:
        draw_game_screen()
    elif game_state == END:
        draw_end_screen()

    # Define the draw_end_screen function here
    def draw_end_screen():
        # Add the code to draw the end screen here
        pass

    # Define the draw_start_screen function here
    def draw_start_screen():
        screen.fill(WHITE)
    
        # Add the header text here
        header_text = TITLE_FONT.render("Watch Your Thoughts Grow", True, BLACK)
        header_text_rect = header_text.get_rect(center=(WIDTH // 2, 50))
        screen.blit(header_text, header_text_rect)
        menu_animation_progress += 0.01
        if menu_animation_progress > 1:
            menu_animation_progress = 1

        # ----- Start of the new code section for menu animation -----
        circle_y_offset = menu_circles_start_y - (menu_circles_start_y - menu_circles_positions[0][1]) * menu_animation_progress
        pygame.draw.circle(screen, menu_circles[0], (menu_circles_positions[0][0], int(circle_y_offset)), menu_circles_radius)

        circle_y_offset = menu_circles_start_y - (menu_circles_start_y - menu_circles_positions[2][1]) * menu_animation_progress
        pygame.draw.circle(screen, menu_circles[2], (menu_circles_positions[2][0], int(circle_y_offset)), menu_circles_radius)

        if menu_animation_progress == 1:
            circle_y_offset = menu_circles_start_y - (menu_circles_start_y - menu_circles_positions[1][1]) * menu_animation_progress
            pygame.draw.circle(screen, menu_circles[1], (menu_circles_positions[1][0], int(circle_y_offset)), menu_circles_radius)

            # Render and draw the "Start" text
            start_text = TITLE_FONT.render("Start", True, WHITE)
            start_text_rect = start_text.get_rect(center=(menu_circles_positions[1][0], int(circle_y_offset)))
            screen.blit(start_text, start_text_rect)

        # Render the instructions for the game
        menu_instructions = [
            "Take a distressing thought you are experiencing and break it into five parts and place them into the circles.",
            "When you get to the last circle, put your thought in and press return (enter),",
            "read the message, and click on the green circle. You will then challenge each",
            "negative part of the thought with a positive one, press return (enter) on the last circle, and click",
            "the green circle to start over."
        ]
        for i, line in enumerate(menu_instructions):
            menu_instruction_text = INSTRUCTION_FONT.render(line, True, BLACK)
            screen.blit(menu_instruction_text, (WIDTH // 2 - menu_instruction_text.get_width() // 2, 100 + i * 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and menu:
            circle_x, circle_y = menu_circles_positions[1]
            offset = max(0, -menu_circles_start_y * (1 - menu_animation_progress))
            if ((mouse_x - circle_x) ** 2 + (mouse_y - (circle_y + offset)) ** 2) < menu_circles_radius ** 2:
                game_state = GAME

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicked
            if green_circle_visible:
                # Check if the user clicked the green circle
                mouse_x, mouse_y = pygame.mouse.get_pos()
                distance = ((circle_positions[2][0] - mouse_x) ** 2 + (circle_positions[2][1] - mouse_y) ** 2) ** 0.5

                if distance <= CIRCLE_RADIUS:
                    if not end_screen:
                        texts = [''] * 5
                        green_circle_visible = False
                        user_clicked_green_circle = not user_clicked_green_circle
                    
                        # Check if the user clicked the green circle for the second time
                        if user_clicked_green_circle:
                            end_screen = True
                    else:
                        end_screen = False

    pygame.display.flip()
    clock.tick(FPS)
    continue

else:
    # All the code after the menu section
    screen.fill(WHITE)
    mouse_x, mouse_y = pygame.mouse.get_pos()

# Handle events
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        if green_circle_visible:
            mini_circle_radius = 10  # Define the variable, choose an appropriate value based on your game design
            mini_circle_x, mini_circle_y = circle_positions[2][0], circle_positions[2][1] + CIRCLE_RADIUS + mini_circle_radius + 20
            if (mouse_x - mini_circle_x) ** 2 + (mouse_y - mini_circle_y) ** 2 < mini_circle_radius ** 2:

                if not end_screen:
                    texts = [''] * 5
                    green_circle_visible = False
                    user_clicked_green_circle = not user_clicked_green_circle
                else:
                    end_screen = False

        # Check if any circle is clicked
        for i, (circle_x, circle_y) in enumerate(circle_positions):
            if (mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2 < CIRCLE_RADIUS ** 2:
                active_text_input = i
                break
        else:
            active_text_input = -1

    if event.type == pygame.KEYDOWN:
        if active_text_input != -1:
            if event.key == pygame.K_RETURN and active_text_input == 4:
                green_circle_visible = True
            elif event.key == pygame.K_BACKSPACE:
                texts[active_text_input] = texts[active_text_input][:-1]
            else:
                texts[active_text_input] += event.unicode

        if event.key == pygame.K_RETURN and active_text_input == 4:
            green_circle_visible = True

# Update opening progress
if opening_progress < len(circle_positions):
    opening_progress += 0.05  # Adjust this value to control the animation speed

    # Draw the title and instructions
    title_text = TITLE_FONT.render('Watch Your Thoughts Grow', True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 10))

    instruction_lines = [
        'Put in a thought and watch it grow. Place your distressing thought in the first circle,',
        'and in the following circles, break it down piece by piece to watch how your initial',
        'distressing thought expanded through the five circles. Starting from beginning to end,',
        'left to right.'
    ]

    for i, line in enumerate(instruction_lines):
        instruction_text = INSTRUCTION_FONT.render(line, True, BLACK)
        screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, 80 + i * 20))

    # Check if all circles have text
    all_circles_filled = all(bool(text) for text in texts)

    # Drawing the circles and the text
    for i, (circle_x, circle_y) in enumerate(circle_positions[:round(opening_progress)]):
        color = circle_colors[i]

        # Draw the circle
        if (mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2 < CIRCLE_RADIUS ** 2:
            pygame.draw.circle(screen, WHITE, (circle_x, circle_y), CIRCLE_RADIUS)
            pygame.draw.circle(screen, color, (circle_x, circle_y), CIRCLE_RADIUS, CIRCLE_OUTLINE)
        else:
            pygame.draw.circle(screen, color, (circle_x, circle_y), CIRCLE_RADIUS)

        # Draw the text inside the circle
        text = texts[i]
        text_surface = CIRCLE_TEXT_FONT.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(circle_x, circle_y))
        screen.blit(text_surface, text_rect)
    
    if all_circles_filled and green_circle_visible:
        # Draw mini circle under circle 3
        mini_circle_color = (0, 175, 66)
        mini_circle_radius = 25
        mini_circle_x, mini_circle_y = circle_positions[2][0], circle_positions[2][1] + CIRCLE_RADIUS + mini_circle_radius + 20
        pygame.draw.circle(screen, mini_circle_color, (mini_circle_x, mini_circle_y), mini_circle_radius)

        if not user_clicked_green_circle:
            reflection_text = (
                "Reflect on the changing nature of your negative thoughts. "
                "How can you challenge these negative thoughts and replace them with positive ones? "
                "How can you shift your perspective in the future to avoid experiencing these negative thoughts? "
                "Would you like to challenge these negative thoughts and place positive ones in them? Click the green button above!"
            )
        else:
            reflection_text = (
                "Great job! Doesn't it feel better to challenge those negative thoughts with positive ones?"
            )

        reflection_lines = reflection_text.split(" ")
        line_length = 0
        line_start = 0
        current_line = 0
        max_line_length = 50

        for i, word in enumerate(reflection_lines):
            line_length += len(word) + 1
            if line_length > max_line_length or i == len(reflection_lines) - 1:
                line = " ".join(reflection_lines[line_start:i+1])
                reflection_surface = INSTRUCTION_FONT.render(line, True, BLACK)
                reflection_rect = reflection_surface.get_rect(center=(WIDTH // 2, circle_positions[2][1] + CIRCLE_RADIUS + 100 + 20 * current_line))
                screen.blit(reflection_surface, reflection_rect)
                line_length = 0
                line_start = i + 1
                current_line += 1

def draw_end_screen():
    screen.fill(WHITE)

    # Draw the rainbow pattern for the first set of answers
    for i, (circle_x, circle_y) in enumerate(circle_positions):
        color = circle_colors[i]
        pygame.draw.circle(screen, color, (circle_x, circle_y - CIRCLE_RADIUS - 10), CIRCLE_RADIUS)

        text = texts[i]
        text_surface = CIRCLE_TEXT_FONT.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(circle_x, circle_y - CIRCLE_RADIUS - 10))
        screen.blit(text_surface, text_rect)

    # Draw the rainbow pattern for the second set of answers
    for i, (circle_x, circle_y) in enumerate(circle_positions):
        color = circle_colors[i]
        pygame.draw.circle(screen, color, (circle_x, circle_y + CIRCLE_RADIUS + 10), CIRCLE_RADIUS)

        text = texts[i]
        text_surface = CIRCLE_TEXT_FONT.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(circle_x, circle_y + CIRCLE_RADIUS + 10))
        screen.blit(text_surface, text_rect)

    # Draw the mini green circle for restarting the game
    mini_circle_color = (0, 175, 66)
    mini_circle_radius = 25
    mini_circle_x, mini_circle_y = circle_positions[2][0], circle_positions[2][1] + CIRCLE_RADIUS * 3 + 20
    pygame.draw.circle(screen, mini_circle_color, (mini_circle_x, mini_circle_y), mini_circle_radius)

    # Draw the text under the mini green circle
    restart_text = "Great job! Click the green circle if you would like to begin again!"
    restart_surface = reflection_font.render(restart_text, True, BLACK)
    restart_rect = restart_surface.get_rect(center=(WIDTH // 2, mini_circle_y + mini_circle_radius + 20))
    screen.blit(restart_surface, restart_rect)


    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()