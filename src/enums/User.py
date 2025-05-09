from enum import StrEnum, auto


class User(StrEnum):
    STANDARD_USER = auto()
    LOCKED_OUT_USER = auto()
    PROBLEM_USER = auto()
    PERFORMANCE_GLITCH_USER = auto()
