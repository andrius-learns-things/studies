from abc import ABC, abstractmethod


class Provider(ABC):

    # Provider meta props

    @property
    @abstractmethod
    def name(self):
        pass

    # Hit count experiment

    @abstractmethod
    def get_hit_count(self):
        pass

    # Single entity experiment

    @abstractmethod
    def ensure_empty_person_structure(self):
        pass

    @abstractmethod
    def register_person(self, person):
        pass

    @abstractmethod
    def search_persons(self, field, value):
        pass

    @abstractmethod
    def add_person_indexes(self):
        pass

    # Two entities experiment

    @abstractmethod
    def ensure_empty_org_structures(self):
        pass

    @abstractmethod
    def register_org(self, org, registration):
        pass

    @abstractmethod
    def get_last_registered_orgs(self, subsystem):
        pass
