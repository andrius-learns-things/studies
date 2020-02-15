from abc import ABC, abstractmethod


class Provider(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def get_hit_count(self):
        pass

    @abstractmethod
    def clear_persons(self):
        pass

    @abstractmethod
    def register_person(self, person):
        pass

    @abstractmethod
    def search_persons(self, field, value):
        pass
