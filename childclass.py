from abc import ABC, abstractmethod


class Aircraft(ABC):

    @abstractmethod
    def fly(self):
        pass


class Jet(Aircraft):
    pass