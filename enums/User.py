from enum import Enum


class User(Enum):
    STANDARD_USER = "standard_user"
    LOCKED_OUT_USER = "locked_out_user"
    PROBLEM_USER = "problem_user"
    PERFORMANCE_GLITCH_USER = "performance_glitch_user"
