from abc import ABC, abstractmethod


class BaseCategory(ABC):
    @classmethod
    @abstractmethod
    def __str__(self):
        pass
