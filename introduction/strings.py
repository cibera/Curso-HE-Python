class Strings:
    singleQuotes = 'Im a string with single quotes'
    doubleQuotes = "Im a string with double quotes"
    tripleQuotes = '''Im a string with triple quotes
    multiline'''
    scapingString = "C:\\User\\Username\\Documents"
    rawString = r"Memory \x47\x65\x65\x6b\x73"
    formatString1 = "{} {} {}".format("Somos", "Ciberseguridad", "para todos")
    formatString2 = "{1} {0} {2}".format("Esto", "va", "primero")
    formatString3 = "{b} {c} {a}".format(a="Cibera", b="Servicios de", c="Ciberseguridad")
    formatString4 = "Number {0} in binary is {0:b}".format(20)
    formatString5 = "Number {0} in decimal (float) is {0:3f}".format(1 / 3)
    formatString6 = "|{:<10}|{:^10}|{:>10}|".format('Formato', 'de', 'Tabla')

    @staticmethod
    def print_char_at(string, place):
        print(string[place])

    @staticmethod
    def slicing_string(string, range):
        print(string[range])

    @staticmethod
    def old_style_string():
        integer = 1234567
        print("Old style printing a integer %d" % integer)
