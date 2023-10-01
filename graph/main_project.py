import pygame
import sys
import color
from graph_ui import Graph
from input_box import InputBox
import equation.equation_to_lines as eqTolines
import equation.string_to_equatuion as strToeq
GRAPH_RESOLUTION=20
def main():
   pygame.init() 
   SCREEN_WIDTH ,SCREEN_HEIGHT =1080,760
   screen=pygame.display.set_mode((1080,760))
   equation=None
   lines=[]
   graph=Graph(x=0,y=0,screen=screen,width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
   def onUserInput(inputBox:InputBox):
       input=inputBox.text
       try:
           equation=strToeq.convert_to_standard_form(input)
           inputBox.text=str(equation)
           contour=eqTolines.equation_to_line_func(equation)
           nonlocal lines
           lines=contour(-graph.max_x(),graph.max_x(),-graph.max_y(),graph.max_y(),graph.max_x()*GRAPH_RESOLUTION,graph.max_y()*GRAPH_RESOLUTION)
           print(lines)
       except:
           raise ValueError("Invalid equation is given")
   inbox=InputBox(screen,x=10,y=700,width=1060,height=50,onEnter=onUserInput)
   running=True
   while running:
        for event in pygame.event.get():
            inbox.handle_event(event)
            if event.type == pygame.QUIT:
                running = False
        screen.fill(color.WHITE)
        # Draw the graph
        graph.draw()

        for x in lines:graph.draw_linesC(x)
        inbox.draw()
        pygame.display.flip()
   pygame.quit()
   sys.exit()

if __name__=="__main__":
    main()
 

   
