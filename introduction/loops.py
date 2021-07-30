class Loops:
    tuple = (1, 2, 3, 4, 5, 6)
    array = [1, 2, 3, 4, 5, 6]
    dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}
    set = {1, 2, 3, 4, 5, 6, 6}
    range = range(1, 6)

    @staticmethod
    def loop_tuple():
        print("Tuple")
        for element in Loops.tuple:
            print(element)

    @staticmethod
    def loop_array():
        print("Array")
        for element in Loops.array:
            print(element)


    @staticmethod
    def loop_dict():
        print("Dict")
        for key in Loops.dict:
            print(f"{key}: {Loops.dict[key]}")


    @staticmethod
    def loop_set():
        print("Set")
        for element in Loops.set:
            print(element)


    @staticmethod
    def loop_range():
        print("Range")
        for value in Loops.range:
            print(value)