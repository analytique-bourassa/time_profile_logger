NumberTypes = (int, float, complex)

class Validator():

    @staticmethod
    def check_type(value, type_):

        if not isinstance(value, type_):
            raise TypeError("The value {} must be of type {}".format(value, type_))

    @staticmethod
    def check_value_strictly_positive(value):

        if not value > 0:
            raise ValueError("The value {} must be of stictly positive".format(value))

    @staticmethod
    def check_value_is_a_number(value):

        if not isinstance(value, NumberTypes):
            raise TypeError("The value {} must be a number".format(value))



