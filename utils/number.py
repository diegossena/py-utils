import time


class FibbonacciCounter:
  def __init__(self):
    self.previous = 0
    self.current = 1

  def next(self):
    res = self.previous
    aux = self.current
    self.current = self.previous + self.current
    self.previous = aux
    return res


def getNoFibonacciNumber(index: int):
  fibbonacciCounter = FibbonacciCounter()

  current = fibbonacciCounter.next()
  previous = 0

  i = 0

  while True:
    previous += 1
    while previous < current:
      i += 1
      if i == index:
        return previous
      previous += 1
    previous = current
    current = fibbonacciCounter.next()


def clamp(number: int, lower: int, higher: int):
  return min(max(number, lower), higher)


def getUniqueID() -> int:
  GETUNIQUEID_EPOCH = 1675220400000
  GETUNIQUEID_MAX_SEQUENCE = 1023
  GETUNIQUEID_NODE = 0
  currentTime = int(time.time_ns() / 1000000)
  uidTime = currentTime - GETUNIQUEID_EPOCH

  getUniqueID.__sequence = (
      getUniqueID.__sequence + 1
  ) & GETUNIQUEID_MAX_SEQUENCE if uidTime == getUniqueID.__lastTimestamp else 0
  getUniqueID.__lastTimestamp = uidTime

  return uidTime << 22 | GETUNIQUEID_NODE << 10 | getUniqueID.__sequence


getUniqueID.__sequence = 0
getUniqueID.__lastTimestamp = 0
