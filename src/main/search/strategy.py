from abc import ABC


class Strategy(ABC):

    def do_action(self, selector) -> str:
        pass
