from enum import Enum


class PetType(Enum):
    cat = 1
    dog = 2


def str_to_enum(enum_string):
    try:
        return PetType(enum_string)
    except ValueError:
        raise ValueError(f"Неверное значение '{enum_string}' для перечисления "
                         f"{PetType.__name__}")

