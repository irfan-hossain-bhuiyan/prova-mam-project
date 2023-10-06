
import sympy as sp

def convert_to_standard_form(equation_str):
    # Define symbols
    x, y = sp.symbols('x y')
    eqLeftStr,eqRightStr=equation_str.split("=",1)
    try:
        # Parse the input equation string into a SymPy expression
        eqLeft = sp.sympify(eqLeftStr)
        eqRight= sp.sympify(eqRightStr)

        # Ensure the result is an equation (Equality type)
            # Subtract the right-hand side from both sides to get the standard form
        standard_form = eqLeft - eqRight
        return standard_form

    except sp.SympifyError:
        raise ValueError("Invalid equation string.")
    except:
        raise ValueError("All other issue.")

# Example usage:
def main():
    equation_str = "x**2 + y**2 = 4"
    standard_equation = convert_to_standard_form(equation_str)
    print(standard_equation)
if __name__=="__main__":
    main()
