from threading import Semaphore
from collections import deque

class BoundedQueue:
    def __init__(self, cap:int) -> None:
        self.q_empty = Semaphore(cap)
        self.q_filled = Semaphore(0)
        self.dq = deque()
    
    def enqueue(self, val):
        self.q_empty.acquire()
        self.dq.append(val)
        self.q_filled.release()
    
    def dequeue(self) -> int:
        self.q_filled.acquire()
        ele = self.dq.popleft()
        self.q_empty.release()
        return ele

    def size(self):
        return len(self.dq)