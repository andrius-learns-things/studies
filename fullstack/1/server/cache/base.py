from abc import ABC, abstractmethod


class BaseCacheProvider(ABC):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass
