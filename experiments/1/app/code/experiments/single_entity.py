from .base import Experiment

NUM = 100


class SingleEntityExperiment(Experiment):
    @property
    def name(self):
        return "Single entity experiment"

    def run_the_experiment(self, provider):

        output = []

        self._experiment_init(provider, output)
        self._experiment_register(provider, output)
        self._experiment_search(provider, output)
        self._experiment_add_index(provider, output)
        self._experiment_search(provider, output)

        return output

    def _experiment_init(self, provider, output):
        def func():
            provider.ensure_empty_person_structure()

        self._measure(output, "Init", func)

    def _experiment_register(self, provider, output):
        def func():
            persons = self._generate_persons(NUM)
            for person in persons:
                provider.register_person(person)

        self._measure(output, "Register", func)

    def _experiment_search(self, provider, output):
        def func():
            searches = [
                {"field": "first_name", "value": "_", "expected_result_count": 0},
                {"field": "first_name", "value": "A", "expected_result_count": 1},
                {"field": "first_name", "value": "BB", "expected_result_count": 1},
            ]
            for search in searches:
                output.append(self._do_search(provider, search))

        self._measure(output, "Search", func)

    def _experiment_add_index(self, provider, output):
        def func():
            provider.add_person_indexes()

        self._measure(output, "Add indexes", func)

    def _do_search(self, provider, search):
        try:
            results = provider.search_persons(
                field=search["field"], value=search["value"]
            )
        except Exception as ex:
            if str(ex) == "Too much":
                return "Too much to handle"
            else:
                raise ex

        result = "PASS" if len(results) == search["expected_result_count"] else "FAIL"

        return "Search by {} returned {}, expected {} | {}".format(
            search["field"], len(results), search["expected_result_count"], result
        )

    def _generate_persons(self, num):

        results = []
        for i in range(num):
            results.append(
                {
                    "person_id": "PID_{}".format(i),
                    "first_name": self._get_name_from_num(i),
                    "last_name": self._get_name_from_num(i),
                }
            )

        return results

    def _get_name_from_num(self, num):

        if num == 0:
            return "A"

        txt = ""
        num_to_divide = num

        while num_to_divide > 0:
            digit = num_to_divide % 10
            num_to_divide = num_to_divide // 10
            txt = chr(65 + digit) + txt

        return txt
