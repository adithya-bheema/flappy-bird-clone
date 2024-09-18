import pygame
import random
import os

# Initialize pygame 
pygame.init()

# Game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRAVITY = 0.6
FLAP_STRENGTH = -8
PIPE_GAP = 150
PIPE_WIDTH = 60
PIPE_SPEED = 6
BIRD_WIDTH = 30
BIRD_HEIGHT = 30
GROUND_HEIGHT = 100
FPS = 60

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load images with resizing
def load_image(filename, size):
    image = pygame.image.load(os.path.join('assets', filename))
    return pygame.transform.scale(image, size)

# Resize dimensions
BIRD_SIZE = (BIRD_WIDTH, BIRD_HEIGHT)
PIPE_SIZE = (PIPE_WIDTH, SCREEN_HEIGHT)  # Keep the width fixed, height variable

bird_image = load_image('bird.png', BIRD_SIZE)
pipe_image = load_image('pipe.png', PIPE_SIZE)
background_image = load_image('background.png', (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load sound effects
def load_sound(filename):
    return pygame.mixer.Sound(os.path.join('assets', filename))

flap_sound = load_sound('flap.wav')
score_sound = load_sound('score.wav')
game_over_sound = load_sound('game_over.wav')

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')  # Corrected line

# Bird class
class Bird:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def flap(self):
        self.velocity = FLAP_STRENGTH
        flap_sound.play()  # Play flap sound

    def draw(self, screen):
        screen.blit(bird_image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)

# Constants for pipe generation
MIN_PIPE_HEIGHT = 100  # Minimum height for the top pipe
PIPE_GAP = 150  # Fixed gap size for bird to pass through

# Pipe class
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        # Generate the height of the top pipe ensuring there's room for the gap
        self.height = random.randint(MIN_PIPE_HEIGHT, SCREEN_HEIGHT - PIPE_GAP - GROUND_HEIGHT)
        self.passed = False

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self, screen):
        # Draw the top pipe (flipped upside down)
        screen.blit(pygame.transform.flip(pipe_image, False, True), (self.x, self.height - SCREEN_HEIGHT))

        # Draw the bottom pipe (normal)
        screen.blit(pipe_image, (self.x, self.height + PIPE_GAP))

    def get_rects(self):
        top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT)
        return top_rect, bottom_rect

# Game over text with score display
def game_over_text(score):
    font = pygame.font.SysFont(None, 48)
    # Display 'Game Over'
    text = font.render('Game Over', True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 - 50))

    # Display final score
    score_text = font.render(f'Your Score: {score}', True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 10))

# Draw start button
def draw_start_button():
    font = pygame.font.SysFont(None, 48)
    button_rect = pygame.Rect(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2, 50)
    pygame.draw.rect(screen, RED, button_rect)
    text = font.render('Start', True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
    return button_rect

# Main menu
def main_menu():
    waiting = True
    while waiting:
        screen.fill(WHITE)
        button_rect = draw_start_button()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    waiting = False

        pygame.display.update()

# Main game loop
def main_game():
    bird = Bird()
    pipes = []
    score = 0
    high_score = 0
    clock = pygame.time.Clock()

    def add_pipe():
        pipes.append(Pipe())

    def check_collision():
        bird_rect = bird.get_rect()
        if bird.y > SCREEN_HEIGHT - GROUND_HEIGHT or bird.y < 0:
            return True
        for pipe in pipes:
            top_rect, bottom_rect = pipe.get_rects()
            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                return True
        return False

    # Game loop
    running = True
    frame_count = 0
    while running:
        screen.blit(background_image, (0, 0))  # Draw background
        frame_count += 1

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        # Update bird and pipes
        bird.update()
        if frame_count % 100 == 0:
            add_pipe()

        for pipe in pipes:
            pipe.update()
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
            pipe.draw(screen)

        bird.draw(screen)

        # Check collision and update score
        if check_collision():
            game_over_sound.play()  # Play game over sound
            game_over_text(score)  # Show game over text and score
            pygame.display.flip()
            pygame.time.wait(2000)
            return  # Exit to main_menu for restart

        # Update score: Increment when bird passes the pipe
        for pipe in pipes:
            if not pipe.passed and bird.x > pipe.x + PIPE_WIDTH:
                pipe.passed = True
                score += 1
                score_sound.play()  # Play score sound when passing a pipe

        # Display score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    while True:
        main_menu()  # Show the start button
        main_game()  # Start the game
