import pygame
import sys
from typing import Optional, Callable

# Constants for colors

from external_dependencies.color import BLACK,CYAN,WHITE
class InputBox:
    def __init__(
        self,
        screen: pygame.Surface,
        x: int,
        y: int,
        width: int,
        height: int,
        font=None,
        rect_color: pygame.Color = CYAN,
        font_color: pygame.Color = BLACK,
        placeholder:str="",
        placeholder_color:pygame.Color=pygame.Color(230,230,230),
        onEnter: Optional[Callable[['InputBox'], None]] = None,
        active: bool = True,
        cursor_blink_interval: int = 500,  # Blink interval in milliseconds
    ):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color = CYAN
        self.text = ''
        self.font = pygame.font.Font(None, 32) if font is None else font
        self.active = active
        self.onEnter = onEnter
        self.font_color = font_color
        self.rect_color = rect_color
        self.cursor_visible = False
        self.cursor_blink_interval = cursor_blink_interval
        self.last_cursor_toggle = pygame.time.get_ticks()
        self.cursor_position = 0  # Initial cursor position
        self.placeholder = placeholder
        self.placeholder_color=placeholder_color
    def handle_event(self, event):
        # Checking if the input box was clicked or not.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.cursor_visible = True
            else:
                self.active = False
                self.cursor_visible = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.onEnter is not None:
                        self.onEnter(self)
                elif event.key == pygame.K_BACKSPACE:
                    if self.cursor_position > 0:
                        self.text = self.text[:self.cursor_position - 1] + \
                        self.text[self.cursor_position:]
                        self.cursor_position -= 1
                elif event.key == pygame.K_LEFT:
                    if self.cursor_position > 0:
                        self.cursor_position -= 1
                elif event.key == pygame.K_RIGHT:
                    if self.cursor_position < len(self.text):
                        self.cursor_position += 1
                else:
                    self.text = self.text[:self.cursor_position] + event.unicode \
                            + self.text[self.cursor_position:]
                    self.cursor_position += 1

    def draw(self):
        self.update_cursor()
        pygame.draw.rect(self.screen, self.rect_color, self.rect, 2)
        if self.text:
            txt_surface = self.font.render(self.text, True, self.font_color)
        else:
            txt_surface = self.font.render(self.placeholder, True,\
                    self.placeholder_color)
        cursor_x = self.rect.x + 5 + self.font.size(self.text[:self.cursor_position])[0]

        if self.cursor_visible and self.active:
            cursor_y = self.rect.y + 5
            pygame.draw.line(self.screen, self.font_color, (cursor_x, cursor_y), \
                    (cursor_x, cursor_y + self.font.get_height()), 2)

        self.screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def update_cursor(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_cursor_toggle > self.cursor_blink_interval:
            self.cursor_visible = not self.cursor_visible
            self.last_cursor_toggle = current_time

def main():
    pygame.init()
    # Initialize Pygame window
    screen_width, screen_height = 1600, 900
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Input Box Example")

    # Initialize font
    font = pygame.font.Font(None, 32)

    # Create an InputBox instance
    input_box = InputBox(screen, 100, 50, 200, 40,\
            font, onEnter=lambda x: print(x.text),placeholder="Enter your age:")

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

if __name__ == "__main__":
    main()
