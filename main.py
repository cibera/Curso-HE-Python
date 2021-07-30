from introduction.variables import type_of_variables, dynamic_variables
from introduction.conditionals import evaluators
from exercises.tcp_client import connect_tcp_with
from introduction.loops import Loops
from introduction.strings import Strings
from exercises.sockets import ClientUDP, ServerTCP, ClientTCP




if __name__ == '__main__':
    type_of_variables()

    variable = 1
    print(variable)
    variable = dynamic_variables(variable)
    print(variable)
    variable = True
    print(variable)

    response = connect_tcp_with("www.cibera.co", 80)
    print(response)

    evaluators()

    Loops.loop_tuple()
    Loops.loop_array()
    Loops.loop_dict()
    Loops.loop_set()
    Loops.loop_range()

    Strings.old_style_string()








