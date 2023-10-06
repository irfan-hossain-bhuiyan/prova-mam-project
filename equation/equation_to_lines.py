import numpy as np
from contourpy import contour_generator
import sympy as sp
x,y=sp.symbols("x,y")
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
def main():
    equation=x**2-y
    contour_function=equation_to_line_func(equation)
    print(contour_function(-3,3,-15,15,30,150))

if __name__=="__main__":
    main()
