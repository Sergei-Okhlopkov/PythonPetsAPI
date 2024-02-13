from enum import Enum


class PetType(Enum):
    cat = 1
    dog = 2


def str_to_enum(enum_string: str):
    try:
        return PetType[enum_string.lower()]
    except Exception:
        raise Exception(f"Неверное значение '{enum_string}' для type. Возможные занчения: {', '.join([name.name for name in PetType])} ")

