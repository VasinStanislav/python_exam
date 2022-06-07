from enum import Enum


class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6


class StateMachine:
    def __init__(self):
        self.state = State.A

    # update is kinda built-in method

    def update(self, transaction):
        self.state, signal = transaction[self.state]
        return signal

    def clone(self):
        return self.update({
            State.A: [State.B, 0],
            State.C: [State.D, 3],
            State.D: [State.E, 5],
            State.E: [State.F, 7],
            State.F: [State.G, 8]
        })

    def trace(self):
        return self.update({
            State.A: [State.C, 1],
            State.B: [State.C, 2],
            State.C: [State.G, 4],
            State.D: [State.D, 6],
            State.F: [State.C, 9]
        })


def main():
    return StateMachine()


o = main()
print(o.clone())
print(o.trace())
print(o.clone())
print(o.clone())
print(o.clone())
print(o.trace())
print(o.clone())
print(o.trace())
print(o.clone())
print(o.clone())
print(o.trace())
print(o.trace())
