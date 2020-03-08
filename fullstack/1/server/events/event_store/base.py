from abc import ABC, abstractmethod


class BaseEventStore(ABC):
    @abstractmethod
    def register_new_event(self, event):
        pass

    @abstractmethod
    def get_events(self, start_index, end_index=None):
        pass
