import pygame
import sys
import sympy
import numpy as np
from external_dependencies.color import BLACK,WHITE
from ui.ui_component_trait import Tcomponent
GRID_COLOR = (200, 200, 200)
    
class Graph(Tcomponent):
    def __init__(self,screen, x, y, width, height, one_unit=1, grid_spacing=30,font=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.one_unit = one_unit
        self.grid_spacing = grid_spacing
        self.screen=screen
        self.font=pygame.font.Font(None,32) if font is None else font
        self.lines=[]
    def scale(self) -> float:
        return self.grid_spacing / self.one_unit
    def __x_lines(self):
        return self.rect.width//(2*self.grid_spacing)
    def __y_lines(self):
        return self.rect.height//(2*self.grid_spacing)
    def max_x(self):
        return self.__x_lines()*self.one_unit
    def max_y(self):
        return self.__y_lines()*self.one_unit   
    def to_screen_coords(self, points):
        # Convert graph coordinates (as a NumPy array) to screen coordinates (as a NumPy array)
        screen_x = np.int32(self.rect.centerx + points[:, 0] * self.scale())
        screen_y = np.int32(self.rect.centery - points[:, 1] * self.scale())

        # Create a NumPy array of screen coordinates
        screen_coords = np.column_stack((screen_x, screen_y))
        return screen_coords
    def to_screen_coord(self,x,y):
        screen_x=self.rect.centerx+x*self.scale()
        screen_y=self.rect.centery-y*self.scale()
        return pygame.Vector2(screen_x,screen_y)
    def to_graph_coords(self, points):
        # Convert screen coordinates (as a NumPy array) to graph coordinates (as a NumPy array)
        graph_x = (points[:, 0] - self.rect.centerx) / self.scale()
        graph_y = (self.rect.centery - points[:, 1]) / self.scale()

        # Create a NumPy array of graph coordinates
        graph_coords = np.column_stack((graph_x, graph_y))
        return graph_coords
    def to_graph_coord(self,x,y):
        graph_x=(x-self.rect.centerx)/self.scale()
        graph_y=(self.rect.centery-y)/self.scale()
        return pygame.Vector2(graph_x,graph_y)
   # def draw_lines(self,screen,x_point0,y_point0,x_point1,y_point1,color=BLACK,width=1):
   #     pygame.draw.line(screen, color, self.to_screen_coords(x_point0, y_point0),
   #                          self.to_screen_coords(x_point1, y_point1), width)
    
    def draw_linesS(self, points0, points1, color=BLACK, width=1):
    # Convert the list of points to NumPy arrays
        points0 = np.array(points0)
        points1 = np.array(points1)
    
        # Convert graph coordinates to screen coordinates
        screen_points0 = self.to_screen_coords(points0)
        screen_points1 = self.to_screen_coords(points1)
    
        # Draw lines between the corresponding screen coordinates
        for point0,point1 in zip(screen_points0,screen_points1):
            pygame.draw.line(self.screen, color,point0, point1, width)
    def draw_linesC(self,points,closed=False,color=BLACK,width=1):
        points = np.array(points)
    
        # Convert graph coordinates to screen coordinates
        screen_points = self.to_screen_coords(points)
        pygame.draw.lines(self.screen,color,closed,screen_points,width)
    
    def handle_event(self, event):
        pass

   # def draw_grid(self):
   #     # Draw horizontal grid lines and annotations
   #      y_points=np.linspace(-self.max_y(),self.max_y(),2*self.__y_lines()+1)
   #      x_points=np.linspace(-self.max_x(),self.max_x(),2*self.__x_lines()+1)
   #      max_x=np.full_like(y_points,self.max_x())
   #      max_y=np.full_like(x_points,self.max_y())
   #      y_lines_point0=np.column_stack((-max_x,y_points))
   #      y_lines_point1=np.column_stack((max_x,y_points))
   #      x_lines_point0=np.column_stack((x_points,-max_y))
   #      x_lines_point1=np.column_stack((x_points,max_y))
   #      self.draw_linesS(y_lines_point0,y_lines_point1)
   #      self.draw_linesS(x_lines_point0,x_lines_point1)
       
    def draw_grid(self):
        # Draw horizontal grid lines and annotations
        y_points = np.linspace(-self.max_y(), self.max_y(), 2 * self.__y_lines() + 1)
        x_points = np.linspace(-self.max_x(), self.max_x(), 2 * self.__x_lines() + 1)
        max_x = np.full_like(y_points, self.max_x())
        max_y = np.full_like(x_points, self.max_y())
        y_lines_point0 = np.column_stack((-max_x, y_points))
        y_lines_point1 = np.column_stack((max_x, y_points))
        x_lines_point0 = np.column_stack((x_points, -max_y))
        x_lines_point1 = np.column_stack((x_points, max_y))
        self.draw_linesS(y_lines_point0, y_lines_point1)
        self.draw_linesS(x_lines_point0, x_lines_point1)
    
        # Annotate the grid lines with text numbers
        for y in y_points:
            text = str(int(y))
            text_surface = self.font.render(text, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = self.to_screen_coord(0, y)
            self.screen.blit(text_surface, text_rect)
    
        for x in x_points:
            text = str(int(x))
            text_surface = self.font.render(text, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = self.to_screen_coord(x, 0)
            self.screen.blit(text_surface, text_rect)
    def draw(self):
        self.draw_grid()
        for x in self.lines:
            self.draw_linesC(x,width=3)
def main():
    from equation import equation_to_line_func
    pygame.init()
    
    # Constants for colors
   
    # Initialize Pygame window
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Zoomable Graph with Grid Annotations Example")
    graph = Graph(screen,0, 0, 800, 600, 1, 20)  # Centered at (0, 0) with a scale of 20 pixels per unit and grid spacing of 20 pixels
    x_symbol=sympy.symbols('x')
    y_symbol=sympy.symbols('y')
    contour=equation_to_line_func(x_symbol**2-y_symbol)
    lines=contour(-10,10,-10,10,100,100)
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)
        # Draw the graph
        graph.draw()
        #pygame.draw.lines(screen,BLACK,True,lines)
    
        for x in lines:graph.draw_linesC(x,width=3)
        pygame.display.flip()
        #graph.draw_linesC(lines.to_list())
    
    pygame.quit()
    sys.exit()
if __name__=="__main__":
    main()

