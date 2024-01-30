def __ANSI(code: int):
  return f'\033[{code}m'


class console:
  RESET = __ANSI(0)
  BOLD = __ANSI(1)
  UNDERLINE = __ANSI(4)

  class fore:
    BLACK = __ANSI(30)
    RED = __ANSI(31)
    GREEN = __ANSI(32)
    YELLOW = __ANSI(33)
    BLUE = __ANSI(34)
    MAGENTA = __ANSI(35)
    CYAN = __ANSI(36)
    WHITE = __ANSI(37)
    RESET = __ANSI(39)

    LIGHT_BLACK = __ANSI(90)
    LIGHT_RED = __ANSI(91)
    LIGHT_GREEN = __ANSI(92)
    LIGHT_YELLOW = __ANSI(93)
    LIGHT_BLUE = __ANSI(94)
    LIGHT_MAGENTA = __ANSI(95)
    LIGHT_CYAN = __ANSI(96)
    LIGHT_WHITE = __ANSI(97)

  class back:
    BLACK = __ANSI(40)
    RED = __ANSI(41)
    GREEN = __ANSI(42)
    YELLOW = __ANSI(44)
    BLUE = __ANSI(44)
    MAGENTA = __ANSI(45)
    CYAN = __ANSI(46)
    WHITE = __ANSI(47)
    RESET = __ANSI(49)

    LIGHT_BLACK = __ANSI(100)
    LIGHT_RED = __ANSI(101)
    LIGHT_GREEN = __ANSI(102)
    LIGHT_YELLOW = __ANSI(103)
    LIGHT_BLUE = __ANSI(104)
    LIGHT_MAGENTA = __ANSI(105)
    LIGHT_CYAN = __ANSI(106)
    LIGHT_WHITE = __ANSI(107)
