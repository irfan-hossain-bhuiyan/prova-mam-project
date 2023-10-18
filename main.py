from typing import List
from ui.ui_component_trait import Tcomponent
import pygame
from external_dependencies import color
from ui.graph_ui import Graph
from ui.input_box import InputBox
from equation import equation_to_line_func,convert_to_standard_form,equation_to_graph_render
import sympy as sp
x,y=sp.symbols("x y")
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
   #lines=[]
   graph=Graph(x=0,y=0,screen=screen,width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
   def onInputBoxEnter(inputBox:InputBox):
       input=inputBox.text
       if input=="":
           return
       global equation
       equation_temp=convert_to_standard_form(input)
       if equation_temp is None:
           inputBox.panic("The equation is not valid.")
       else:
          equation=equation_temp
          inputBox.text=str(equation)+"=0"
          equation_to_graph_render(equation,graph,GRAPH_RESOLUTION) 
  
       
   inbox=InputBox(screen,x=from_left(10),y=from_down(60),width=SCREEN_WIDTH-20,height=50,\
           onEnter=onInputBoxEnter,placeholder="Enter equation:",\
           allowed_key='0123456789^*+-=/()xy.',active=True,rect_color=color.RED,placeholder_color=color.DARK_GRAY)
   def onXInputEnter(box:InputBox): 
       global equation
       if equation is None:
           return
       text=box.text
       if text=="":
           return
       try:
           text=float(eval(text))
           #x=sp.symbols("x")
           equation=sp.expand(equation.subs(x,x+text))
           inbox.text=str(equation)+"=0"
           equation_to_graph_render(equation,graph,GRAPH_RESOLUTION)
           box.text=""
       except:
           box.panic("Can't evaluate input.")

   def onYInputEnter(box:InputBox):
       global equation
       if equation is None:
           return
       text=box.text
       if text=="":
           return
       try:
           text=float(eval(text))
           #y=sp.symbols("y")
           equation=sp.expand(equation.subs(y,y+text))
           inbox.text=str(equation)+"=0"
           equation_to_graph_render(equation,graph,GRAPH_RESOLUTION)
           box.text=""
       except:
           box.panic("Can't evaluate input.")



   x_input=InputBox(screen,x=from_right(200),y=from_down(110),width=150,rect_color=color.RED,\
           height=40,onEnter=onXInputEnter,placeholder="Enter x shift:",
                        allowed_key='0123456789^*+-=/().',placeholder_color=color.DARK_GRAY)
   y_input=InputBox(screen,x=from_right(200),y=from_down(160),width=150,rect_color=color.RED,\
           height=40,onEnter=onYInputEnter,placeholder="Enter y shift:",
                    allowed_key='0123456789^*+-=/()',placeholder_color=color.DARK_GRAY)
   components:List[Tcomponent]=[inbox,x_input,y_input,graph]
   running=True
   while running:
       try:
           for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     running = False
                 for component in components:
                         component.handle_event(event)
           screen.fill(color.WHITE)
           for component in components:
                 component.draw()
             # Draw the graph
            # for x in lines:
            #     graph.draw_linesC(x,width=3)
           pygame.display.flip()
       except:
           inbox.panic("Some error occured.Don't know.")
   pygame.quit()

if __name__=="__main__":
    main()
 

   
