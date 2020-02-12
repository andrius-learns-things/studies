from abc import ABC, abstractmethod


class Provider(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def get_hit_count(self):
        pass
