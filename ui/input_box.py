import pygame
import sys
from typing import Optional, Callable

# Constants for colors
from external_dependencies.color import BLACK,CYAN,WHITE,RED
from ui.ui_component_trait import Tcomponent
class InputBox(Tcomponent):
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
        placeholder_color:pygame.Color=pygame.Color(200,200,200),
        onEnter: Optional[Callable[['InputBox'], None]] = None,
        active: bool = False,
        cursor_blink_interval: int = 500,  # Blink interval in milliseconds
        allowed_key=None,
    ):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color = CYAN
        self.__text = ''
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
        self.allowed_key=allowed_key
        self.panic_text = None
    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self,other:str):
        self.__text=other
        self.cursor_position=len(other)
    def panic(self, error: str):
        # Display an error message in red
        self.__text = error
        self.font_color = RED
        self.panic_text = error
    def handle_event(self, event):
        if self.panic_text:
            # If there is a panic message and the user starts typing, 
            #clear the panic state
            if event.type == pygame.KEYDOWN and event.unicode and \
                    event.key not in (pygame.K_RETURN, pygame.K_BACKSPACE):
                self.__text = ''
                self.font_color = BLACK
                self.panic_text = None
        # Checking if the input box was clicked or not.

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
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
                        self.__text = self.__text[:self.cursor_position - 1] + \
                        self.__text[self.cursor_position:]
                        self.cursor_position -= 1
                elif event.key == pygame.K_LEFT:
                    if self.cursor_position > 0:
                        self.cursor_position -= 1
                elif event.key == pygame.K_RIGHT:
                    if self.cursor_position < len(self.__text):
                        self.cursor_position += 1
                elif self.allowed_key is None or event.unicode in self.allowed_key:
                    if event.unicode:
                        self.__text = self.__text[:self.cursor_position] + \
                            event.unicode + self.__text[self.cursor_position:]
                        self.cursor_position += 1

    def draw(self):
        self.update_cursor()
        pygame.draw.rect(self.screen, self.rect_color, self.rect, 2)
        if self.__text:
            txt_surface = self.font.render(self.__text, True, self.font_color)
        else:
            txt_surface = self.font.render(self.placeholder, True,\
                    self.placeholder_color)
        cursor_x = self.rect.x + 5 + self.font.size(self.__text[:self.cursor_position])[0]

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
            font, onEnter=lambda x: print(x.__text),placeholder="Enter your age:")

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
