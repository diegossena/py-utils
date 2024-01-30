def _ANSI(code: int):
  return f'\033[{code}m'


class console:
  RESET = _ANSI(0)
  BOLD = _ANSI(1)
  UNDERLINE = _ANSI(4)

  class fore:
    BLACK = _ANSI(30)
    RED = _ANSI(31)
    GREEN = _ANSI(32)
    YELLOW = _ANSI(33)
    BLUE = _ANSI(34)
    MAGENTA = _ANSI(35)
    CYAN = _ANSI(36)
    WHITE = _ANSI(37)
    RESET = _ANSI(39)

    LIGHT_BLACK = _ANSI(90)
    LIGHT_RED = _ANSI(91)
    LIGHT_GREEN = _ANSI(92)
    LIGHT_YELLOW = _ANSI(93)
    LIGHT_BLUE = _ANSI(94)
    LIGHT_MAGENTA = _ANSI(95)
    LIGHT_CYAN = _ANSI(96)
    LIGHT_WHITE = _ANSI(97)

  class back:
    BLACK = _ANSI(40)
    RED = _ANSI(41)
    GREEN = _ANSI(42)
    YELLOW = _ANSI(44)
    BLUE = _ANSI(44)
    MAGENTA = _ANSI(45)
    CYAN = _ANSI(46)
    WHITE = _ANSI(47)
    RESET = _ANSI(49)

    LIGHT_BLACK = _ANSI(100)
    LIGHT_RED = _ANSI(101)
    LIGHT_GREEN = _ANSI(102)
    LIGHT_YELLOW = _ANSI(103)
    LIGHT_BLUE = _ANSI(104)
    LIGHT_MAGENTA = _ANSI(105)
    LIGHT_CYAN = _ANSI(106)
    LIGHT_WHITE = _ANSI(107)
