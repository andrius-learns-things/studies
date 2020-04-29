from locust import HttpLocust, TaskSet, between


def login(l):
    pass


def logout(l):
    pass


def index(l):
    l.client.get("/")


def use_and_release(l):
    l.client.get("/use-and-release")


def use_and_leak(l):
    l.client.get("/use-and-leak")


class UserBehavior(TaskSet):
    tasks = {index: 2, use_and_release: 1, use_and_leak: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
