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


def main():
    fibbonacciCounter = FibbonacciCounter()
    selected = 1050
    current = fibbonacciCounter.next()
    index = 0
    previous = 0
    while (1):
        previous += 1
        while (previous < current):
            index += 1
            if (index == selected):
                print("result", previous)
                return
            previous += 1
        previous = current
        current = fibbonacciCounter.next()


main()
