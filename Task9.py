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

    def update(self, transitions):
        self.state, signal = transitions[self.state]
        return signal

    def build(self):
        return self.update({
            State.A: [State.B, 0],
            State.C: [State.D, 2],
            State.D: [State.E, 3],
            State.E: [State.B, 6],
            State.F: [State.B, 8]
        })

    def peep(self):
        return self.update({
            State.B: [State.C, 1],
            State.D: [State.A, 4],
            State.E: [State.F, 5],
            State.F: [State.G, 7],
            State.G: [State.E, 9]
        })


def main():
    return StateMachine()
