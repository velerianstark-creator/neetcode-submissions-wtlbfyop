from collections import deque
class MinStack:

    def __init__(self):
        self._container = deque()
        self._min = None

    def push(self, val: int) -> None:
        if not self._container:
            self._container.append((val, val))
        else:
            current_min = self._container[-1][-1]
            self._container.append((val, min(val, current_min)))         

    def pop(self) -> None:
        self._container.pop()


    def top(self) -> int:
        return self._container[-1][0]

    def getMin(self) -> int:
        return self._container[-1][1]

        
