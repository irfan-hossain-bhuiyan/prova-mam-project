import numpy as np
from contourpy import contour_generator
import sympy as sp
from ui.graph_ui import Graph
x,y=sp.symbols("x,y")


#Converting string to equation.Because it doesn't have a result type,
#I am using Value to define error.
def convert_to_standard_form(equation_str):
    # Define symbols
    eqLeftStr,eqRightStr=equation_str.split("=",1)
    try:
        # Parse the input equation string into a SymPy expression
        eqLeft = sp.sympify(eqLeftStr)
        eqRight= sp.sympify(eqRightStr)

        # Ensure the result is an equation (Equality type)
            # Subtract the right-hand side from both sides to get the standard form
        standard_form = eqLeft - eqRight
        return standard_form

    except:
        return None
# Example usage:
def equation_to_line_func(equation):
    equation_function = sp.lambdify((x, y), equation, "numpy")
    def to_lines(xmin,xmax,ymin,ymax,resolutionx,resolutiony):
        x = np.linspace(xmin,xmax,resolutionx)
        y = np.linspace(ymin,ymax,resolutiony)
        X, Y = np.meshgrid(x, y)
        c=contour_generator(z=equation_function(X,Y))
        matrix_lines=c.lines(0)
        graph_lines=matrix_lines/np.array([resolutionx-1,resolutiony-1])*np.array([xmax-xmin,ymax-ymin])\
        +np.array([xmin,ymin])
        return graph_lines
    return to_lines

def equation_to_graph_render(equation,graph:Graph,resolution:int):
    contour=equation_to_line_func(equation)
    graph.lines=contour(-graph.max_x(),graph.max_x(),-graph.max_y(),graph.max_y()\
                   ,graph.max_x()*resolution,graph.max_y()*resolution)

def main():
    equation_str = "x**2 + y**2 = 4"
    equation = convert_to_standard_form(equation_str)
    contour_function=equation_to_line_func(equation)
    print(contour_function(-3,3,-15,15,30,150))

if __name__=="__main__":
    main()
