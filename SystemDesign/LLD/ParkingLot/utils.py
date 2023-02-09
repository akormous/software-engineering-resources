import string
import random

N = 5

class IdGenerator:
    def __init__(self):
        self.size = N

    def generateId(self) -> str:
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k = self.size))