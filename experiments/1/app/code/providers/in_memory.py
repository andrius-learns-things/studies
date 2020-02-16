from .base import Provider

hits = 0

persons = []


class InMemoryProvider(Provider):
    @property
    def name(self):
        return "In memory"

    def get_hit_count(self):
        global hits
        hits = hits + 1
        return hits

    def ensure_empty_person_structure(self):
        global persons
        persons = []

    def register_person(self, person):
        persons.append(person)

    def search_persons(self, field, value):

        results = []

        for p in persons:
            if p[field] == value:
                results.append(p)

        return results
