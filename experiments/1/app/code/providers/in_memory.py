from .base import Provider

hits = 0

persons = []
subsystem_registrations = {}


class InMemoryProvider(Provider):

    # Provider meta props

    @property
    def name(self):
        return "In memory"

    # Hit count experiment

    def get_hit_count(self):
        global hits
        hits = hits + 1
        return hits

    # Single entity experiment

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

    def add_person_indexes(self):
        pass

    # Two entities experiment

    def ensure_empty_org_structures(self):
        pass

    def register_org(self, org, registration):

        subsystem = registration["subsystem"]
        regs = subsystem_registrations.get(subsystem)

        if not regs:
            regs = []
            subsystem_registrations[subsystem] = regs

        regs.append(org)

    def get_last_registered_orgs(self, subsystem):
        regs = subsystem_registrations.get(subsystem)
        return regs if regs else []
