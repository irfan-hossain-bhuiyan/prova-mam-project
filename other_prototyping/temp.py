def transform_equation_string(equation_str):
        transformed_str = ''
        i = 0
        while i < len(equation_str):
            current_char = equation_str[i]
            if current_char.isalpha() and i > 0 and equation_str[i-1].isdigit():
                transformed_str += '*'
            transformed_str += current_char
            i += 1
        return transformed_str    


print(transform_equation_string("3x+4y+3**x=10"))
