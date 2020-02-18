from datetime import datetime
from .base import Experiment
from time import time

NUM = 10000


class TwoEntitiesJoinedExperiment(Experiment):
    @property
    def name(self):
        return "Two entities joined experiment"

    def run_the_experiment(self, provider):

        output = []

        self._experiment_init(provider, output)
        self._experiment_register_orgs(provider, output)
        self._experiment_search_orgs(provider, output)

        return output

    def _experiment_init(self, provider, output):
        def func():
            provider.ensure_empty_org_structures()

        self._measure(output, "Init", func)

    def _experiment_register_orgs(self, provider, output):
        def func():
            registrations = self._generate_registrations()
            for org, r in registrations:
                provider.register_org(org, r)

        self._measure(output, "Register orgs", func)

    def _experiment_search_orgs(self, provider, output):
        def func():
            searches = [
                {"subsystem": "_", "expected_result_count": 0},
                {"subsystem": "I", "expected_result_count": 1},
                {"subsystem": "II", "expected_result_count": 2},
            ]
            for search in searches:
                output.append(self._do_search(provider, search))

        self._measure(output, "Search orgs", func)

    def _measure(self, output, title, function):

        output.append("-")
        output.append("Measuring {}".format(title))

        start_time = time()
        function()
        end_time = time()

        elapsed_time = round(
            (end_time - start_time) * 1000
        )  # x1000 to get ms from secs

        output.append("Time: {}ms".format(elapsed_time))

    def _generate_registrations(self):
        return [
            (
                {"name": "Company A"},
                {"reg_date": datetime(2019, 5, 17), "subsystem": "I"},
            ),
            (
                {"name": "Company A"},
                {"reg_date": datetime(2019, 5, 18), "subsystem": "II"},
            ),
            (
                {"name": "Company B"},
                {"reg_date": datetime(2019, 5, 19), "subsystem": "II"},
            ),
        ]

    def _do_search(self, provider, search):
        try:
            results = provider.get_last_registered_orgs(search["subsystem"])
        except Exception as ex:
            if str(ex) == "Too much":
                return "Too much to handle"
            else:
                raise ex

        result = "PASS" if len(results) == search["expected_result_count"] else "FAIL"

        return "Search by {} returned {}, expected {} | {}".format(
            search["subsystem"], len(results), search["expected_result_count"], result
        )
