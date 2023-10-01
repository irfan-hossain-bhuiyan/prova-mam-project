
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
        screen:pygame.Surface,
        x: int,
        y: int,
        width: int,
        height: int,
        font=None,
        rect_color: pygame.Color = CYAN,
        font_color: pygame.Color = BLACK,
        onEnter: Optional[Callable[['InputBox'], None]] = None,
        active: bool = True,
    ):
        self.screen=screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color = CYAN
        self.text = ''
        self.font=pygame.font.Font(None,32) if font is None else font
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
    def draw(self):
        pygame.draw.rect(self.screen, self.rect_color, self.rect, 2)
        txt_surface = self.font.render(self.text, True, self.font_color)
        self.screen.blit(txt_surface, (self.rect.x + 5,self.rect.y + 5))

def main():
# Initialize Pygame window
    screen_width, screen_height = 1600, 900
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Input Box Example")
    
    # Initialize font
    font = pygame.font.Font(None, 32)
    
    # Create an InputBox instance
    input_box = InputBox(screen,100, 50, 200, 40, font,onEnter=lambda x:print(x.text))
    
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            input_box.handle_event(event)
    
        screen.fill(WHITE)
        input_box.draw()
        # Draw the input box
    
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main()
