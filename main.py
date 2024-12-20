import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)

# Ball class
class Ball:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)
        self.radius = random.randint(10, 30)
        self.color = [random.randint(0, 255) for _ in range(3)]
        self.vx = random.choice([-4, -3, -2, 2, 3, 4])
        self.vy = random.choice([-4, -3, -2, 2, 3, 4])

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off walls
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.vx *= -1
            self.change_color()

        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.vy *= -1
            self.change_color()

    def change_color(self):
        self.color = [random.randint(0, 255) for _ in range(3)]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Setup the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colorful Bouncing Balls")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# List of balls
balls = [Ball() for _ in range(10)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Update and draw balls
    for ball in balls:
        ball.move()
        ball.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
