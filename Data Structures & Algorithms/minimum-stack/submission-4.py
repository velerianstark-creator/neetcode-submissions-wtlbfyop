from collections import deque
class MinStack:

    def __init__(self):
        self._container = deque()
        self._min = None

    def push(self, val: int) -> None:
        if self._min == None:
            self._container.append((val, val))
            self._min = val
        else:
            if self._min <= val:
                self._container.append((val, self._min))
            else:
                self._min = val
                self._container.append((val, self._min))
                


    def pop(self) -> None:
        self._container.pop()
        if len(self._container) > 0:
            self._min = self._container[-1][1]
        else:
            self._min = None

    def top(self) -> int:
        return self._container[-1][0]

    def getMin(self) -> int:
        return self._container[-1][1]

        
