import pygame
import sys
from external_dependencies import color
from ui.graph_ui import Graph
from ui.input_box import InputBox
import equation.equation_to_lines as eqTolines
import equation.string_to_equatuion as strToeq
GRAPH_RESOLUTION=20
equation=None

SCREEN_WIDTH ,SCREEN_HEIGHT =1080,760
def from_left(x:int):
    return x
def from_right(x:int):
    return SCREEN_WIDTH-x
def from_top(y:int):
    return y
def from_down(y:int):
    return SCREEN_HEIGHT-y


def main():
   pygame.init() 
   screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
   lines=[]
   graph=Graph(x=0,y=0,screen=screen,width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
   def onInputBoxEnter(inputBox:InputBox):
       input=inputBox.text
       if input=="":
           return
       try:
           equation=strToeq.convert_to_standard_form(input)
           contour=eqTolines.equation_to_line_func(equation)
           inputBox.text=str(equation)+"=0"
           nonlocal lines
           lines=contour(-graph.max_x(),graph.max_x(),-graph.max_y(),graph.max_y()\
                   ,graph.max_x()*GRAPH_RESOLUTION,graph.max_y()*GRAPH_RESOLUTION)
       except:
           raise ValueError("Invalid equation is given")
   def onXInputEnter(box:InputBox): 
       if equation is None:
           return
       text=box.text
       if text=="":
           return
       box.text=""
       text=float(text)
       #equation=equation as 
       print("text")
   def onYInputEnter(box:InputBox):
        if equation is None:
            return 
        text=box.text
        if text=="":
            return
        box.text=""
        print("text")

        

       ##euation box positioning.
   inbox=InputBox(screen,x=from_left(10),y=from_down(60),width=SCREEN_WIDTH-20,height=50,\
           onEnter=onInputBoxEnter,placeholder="Enter equation:")
   x_input=InputBox(screen,x=from_right(200),y=from_down(110),width=150,\
           height=40,onEnter=onXInputEnter,placeholder="Enter x shift:")
   y_input=InputBox(screen,x=from_right(200),y=from_down(160),width=150,\
           height=40,onEnter=onYInputEnter,placeholder="Enter y shift:")
   components=[inbox,x_input,y_input,graph]
   running=True
   while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for component in components:
                try:
                    component.handle_event(event)
                except:
                    pass
        screen.fill(color.WHITE)
        for component in components:
            component.draw()
        # Draw the graph
        for x in lines:
            graph.draw_linesC(x,width=3)
        pygame.display.flip()
   pygame.quit()
   sys.exit()

if __name__=="__main__":
    main()
 

   
