class Agent:
    def __init__(self):
        self.inteligencja = 0.1
        self.doswiadczenie = 0

    def rozwoj(self):
        self.doswiadczenie += 1
        self.inteligencja += 0.002
