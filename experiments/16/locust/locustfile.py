from locust import HttpLocust, TaskSet, between


def login(l):
    pass


def logout(l):
    pass


def task_index(l):
    l.client.get("/")


def task_use_and_release(l):
    l.client.get("/use-and-release")


def task_use_and_leak(l):
    l.client.get("/use-and-leak")


class UserBehavior(TaskSet):
    tasks = {task_index: 1, task_use_and_release: 1, task_use_and_leak: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1.0, 1.0)
