from .base import Experiment


class SingleEntityExperiment(Experiment):
    @property
    def name(self):
        return "Single entity experiment"

    def run_the_experiment(self, provider):

        persons = [{"person_id": "1", "first_name": "A", "last_name": "B"}]

        for person in persons:
            provider.register_person(person)

        searches = [
            {"field": "first_name", "value": "B", "expected_result_count": 0},
            {"field": "first_name", "value": "A", "expected_result_count": 1},
        ]

        output = []

        for search in searches:

            results = provider.search_persons(
                field=search["field"], value=search["value"]
            )

            result = (
                "PASS" if len(results) == search["expected_result_count"] else "FAIL"
            )

            output.append(
                "Search by {} returned {}, expected {} | {}".format(
                    search["field"],
                    len(results),
                    search["expected_result_count"],
                    result,
                )
            )

        return output
