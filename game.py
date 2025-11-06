import pygame
import random
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 40)

# Game options
choices = ["rock", "paper", "scissors"]

# Scoring
player_score = 0
computer_score = 0


def draw_text(text, x, y):
    label = font.render(text, True, BLACK)
    screen.blit(label, (x, y))


def get_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "Player"
    else:
        return "Computer"


# Button rectangles
rock_btn = pygame.Rect(50, 300, 150, 50)
paper_btn = pygame.Rect(225, 300, 150, 50)
scissors_btn = pygame.Rect(400, 300, 150, 50)

player_choice = None
computer_choice = None
result = ""


while True:
    screen.fill(WHITE)

    draw_text("Rock Paper Scissors", 160, 30)

    # Draw buttons
    pygame.draw.rect(screen, (200, 200, 200), rock_btn)
    pygame.draw.rect(screen, (200, 200, 200), paper_btn)
    pygame.draw.rect(screen, (200, 200, 200), scissors_btn)

    draw_text("Rock", 95, 310)
    draw_text("Paper", 265, 310)
    draw_text("Scissors", 430, 310)

    # Display choices & result
    if player_choice:
        draw_text(f"You chose: {player_choice}", 50, 120)
        draw_text(f"Computer chose: {computer_choice}", 50, 160)
        draw_text(f"Result: {result}", 50, 200)

    # Scoreboard
    draw_text(f"Score -> You: {player_score}  Computer: {computer_score}", 50, 250)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if rock_btn.collidepoint(mouse_pos):
                player_choice = "rock"
            elif paper_btn.collidepoint(mouse_pos):
                player_choice = "paper"
            elif scissors_btn.collidepoint(mouse_pos):
                player_choice = "scissors"
            else:
                continue

            computer_choice = random.choice(choices)
            winner = get_winner(player_choice, computer_choice)

            if winner == "Player":
                result = "You Win!"
                player_score += 1
            elif winner == "Computer":
                result = "You Lose!"
                computer_score += 1
            else:
                result = "It's a Tie!"

    pygame.display.update()
