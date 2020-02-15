from .base import Provider

hits = 0


class InMemoryProvider(Provider):
    @property
    def name(self):
        return "In memory"

    def get_hit_count(self):
        global hits
        hits = hits + 1
        return hits

    def register_person(self, person):
        pass

    def search_persons(self, field, value):
        return []
