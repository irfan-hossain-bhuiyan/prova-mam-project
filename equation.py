import sympy as sp
def xy_shift_input():
    x_shift=float(input("Where do you want to shift the x axis:"))
    y_shift=float(input("Where do you want to shift the y axis:"))
    return (x_shift,y_shift)
def main():
    x,y=sp.symbols('x,y')
    while True:
        equation_str=input("Enter the equation(q for exit):")
        if equation_str=="q":break
        input_equation=sp.simplify(equation_str)
        print("Here is your equation.",sp.simplify(input_equation))
        x_shift,y_shift=xy_shift_input()
        shifted_equation=input_equation.subs({x:x+x_shift,y:y+y_shift})
        ans=sp.simplify(sp.expand(shifted_equation)).__repr__()
        print(ans)
if __name__=="__main__":
    main()
    input("Press enter to exit.")
