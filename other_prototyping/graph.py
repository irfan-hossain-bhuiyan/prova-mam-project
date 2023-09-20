
import pygame
import sys

pygame.init()

# Constants for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRID_COLOR = (200, 200, 200)

# Initialize Pygame window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zoomable Graph with Grid Annotations Example")

class Graph:
    def __init__(self, x, y, width, height, one_unit, grid_spacing):
        self.rect = pygame.Rect(x, y, width, height)
        self.one_unit=one_unit
        self.width=width
        self.height=height
        self.grid_spacing = grid_spacing
        self.__center_x = x + width // 2
        self.__center_y = y + height // 2
        self.__x_lines=width//(2*grid_spacing)
        self.__y_lines=height//(2*grid_spacing)
        self.graph_data = []  # List to store graph data points
    def scale(self)->int:
        return self.grid_spacing/self.one_unit   

    def to_screen_coords(self, point):
        # Convert graph coordinates to screen coordinates
        screen_x = int(self.__center_x + point[0] * self.scale())
        screen_y = int(self.__center_y - point[1] * self.scale())
        return (screen_x, screen_y)

    def to_graph_coords(self, point):
        # Convert screen coordinates to graph coordinates
        graph_x = (point[0] - self.__center_x) / self.scale()
        graph_y = (self.__center_y - point[1]) / self.scale()
        return (graph_x, graph_y)

    def add_data_point(self, point):
        self.graph_data.append(point)

        
    def draw_grid(self, screen):
        # Draw horizontal grid lines and annotations
        for y in range(-self.__y_lines, self.__y_lines+1):
            y_point=y*self.one_unit
            x_point=self.__x_lines*self.one_unit
            pygame.draw.line(screen, GRID_COLOR,self.to_screen_coords((-x_point,y_point)), 
                             self.to_screen_coords((x_point,y_point)),1)

            # Annotate the grid lines with text numbers
            
            text = str(int(y*self.one_unit))
            text_surface = pygame.font.Font(None, 24).render(text, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center =  self.to_screen_coords((0,y_point))
            screen.blit(text_surface, text_rect)

        # Draw vertical grid lines and annotations
#        for x in range(-self.rect.w // 2, self.rect.w // 2, self.grid_spacing):
#            grid_line_x = self.__center_x + x
#            pygame.draw.line(screen, GRID_COLOR, (self.to_graph_coords((grid_line_x, self.rect.top))), (self.to_graph_coords((grid_line_x, self.rect.bottom))), 1)
#
#            # Annotate the grid lines with text numbers
#            if x != 0:
#                text = str(int(x / self.grid_spacing))
#                text_surface = pygame.font.Font(None, 24).render(text, True, BLACK)
#                text_rect = text_surface.get_rect()
#                text_rect.center = (grid_line_x, self.__center_y + 20)
#                screen.blit(text_surface, text_rect)
#
    def draw(self, screen):
        # Draw the graph axes
        #pygame.draw.line(screen, BLACK,self.to_screen_coords((-self.)), (self.__center_x, self.rect.bottom), 2)
        #pygame.draw.line(screen, BLACK, (self.rect.left, self.__center_y), (self.rect.right, self.__center_y), 2)

        # Draw the grid lines and annotations
        self.draw_grid(screen)

        # Draw the graph data points
        if len(self.graph_data) > 1:
            for i in range(1, len(self.graph_data)):
                start_point = self.to_screen_coords(self.graph_data[i - 1])
                end_point = self.to_screen_coords(self.graph_data[i])
                pygame.draw.line(screen, RED, start_point, end_point, 2)

# Create a Graph instance with grid lines and annotations
graph = Graph(0,0,800,600,1,20)  # Centered at (350, 250) with a scale of 20 pixels per unit and grid spacing of 40 pixels

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)

    # Draw the graph
    graph.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
