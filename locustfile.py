#!/usr/bin/env python

from locust import HttpLocust, TaskSet, task

# http://karlandkeke.com/daycare/grade/A?q=&nearby=
# http://karlandkeke.com/daycare/grade/B?q=&nearby=
# http://karlandkeke.com/daycare/grade/C?q=&nearby=
# http://karlandkeke.com/daycare/grade/D?q=&nearby=


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.index()

    @task(6)
    def gradeD(self):
        self.client.get("/daycare/grade/D?q=&nearby=")

    @task(6)
    def gradeC(self):
        self.client.get("/daycare/grade/C?q=&nearby=")

    @task(6)
    def gradeB(self):
        self.client.get("/daycare/grade/B?q=&nearby=")

    @task(6)
    def gradeA(self):
        self.client.get("/daycare/grade/A?q=&nearby=")

    @task(3)
    def index(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    # min_wait = 5000
    # max_wait = 9000
    min_wait = 2000
    max_wait = 9000
