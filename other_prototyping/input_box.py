
import pygame
import sys
from typing import Optional, Callable

pygame.init()

# Constants for colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
CYAN = pygame.Color(0, 255, 255)

class InputBox:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        font: pygame.font.Font,
        rect_color: pygame.Color = CYAN,
        font_color: pygame.Color = BLACK,
        onEnter: Optional[Callable[['InputBox'], None]] = None,
        active: bool = True,
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = CYAN
        self.text = ''
        self.font = font
        self.active = active
        self.onEnter = onEnter
        self.font_color = font_color
        self.rect_color = rect_color

    def handle_event(self, event):
        # Checking if the input box was clicked or not.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = CYAN if self.active else WHITE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.onEnter is not None:
                        self.onEnter(self)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
    def draw(self,screen:pygame.Surface):
        pygame.draw.rect(screen, input_box.rect_color, input_box.rect, 2)
        txt_surface = input_box.font.render(input_box.text, True, input_box.font_color)
        screen.blit(txt_surface, (input_box.rect.x + 5, input_box.rect.y + 5))

# Initialize Pygame window
screen_width, screen_height = 1600, 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Input Box Example")

# Initialize font
font = pygame.font.Font(None, 32)

# Create an InputBox instance
input_box = InputBox(100, 50, 200, 40, font)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        input_box.handle_event(event)

    screen.fill(WHITE)
    input_box.draw(screen)
    # Draw the input box

    pygame.display.flip()

pygame.quit()
sys.exit()
