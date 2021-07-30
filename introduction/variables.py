import math


def type_of_variables():
    variables = []

    integer = 123456789
    variables.append(integer)

    long = int(math.pow(2, 128))
    variables.append(long)

    float = 32.3e18
    variables.append(float)

    string = "asfghjk"
    variables.append(string)

    string_alt = 'asdfghjk'
    variables.append(string_alt)

    boolean = True
    variables.append(boolean)

    hexadecimal = 0x10
    variables.append(hexadecimal)

    octal = 0o10
    variables.append(octal)

    binary = 0b10
    variables.append(binary)

    for x in variables:
        print(f"I'm a {type(x)} type of variable and my value is: {x}")


def dynamic_variables(variable):
    variable = "Now I'm a string"
    return variable
