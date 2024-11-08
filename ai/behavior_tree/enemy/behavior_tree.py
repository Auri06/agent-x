import time

class Node:
    def run(self):
        raise NotImplementedError("This method should be overridden.")

class Sequence(Node):
    def __init__(self, children):
        self.children = children

    def run(self):
        for child in self.children:
            if not child.run():
                return False
        return True

class Selector(Node):
    def __init__(self, children):
        self.children = children

    def run(self):
        for child in self.children:
            if child.run():
                return True
        return False

class Action(Node):
    def __init__(self, action):
        self.action = action

    def run(self):
        return self.action()


class Invert(Node):
    def __init__(self, child):
        self.child = child

    def run(self):
        return not self.child.run()


class Timer(Node):
    def __init__(self, duration, child):
        self.duration = duration
        self.child = child
        self.start_time = None

    def run(self):
        if self.start_time is None:
            self.start_time = time.time()
        if time.time() - self.start_time >= self.duration:
            self.start_time = None
            return self.child.run()
        return False



