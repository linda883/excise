from locust import HttpLocust,TaskSet,task
import subprocess
import json


# This is the TaskSet class.
class UserBehavior(TaskSet):
    # Execute before any task.
    def on_start(self):
        pass

    # the @task takes an optional weight argument.
    @task(1)
    def list_header(self):
        r = self.client.get("/homepage/list_header.html")
        if json.loads((r.content))["result"] != 100:
            r.failure("Got wrong response:"+r.content)

    @task(2)
    def list_goods(self):
        r = self.client.get("/homepage/list_goods.html")
        if json.loads((r.content))["result"] != 100:
            r.failure("Got wrong response:"+r.content)


# This is one HttpLocust class.
class WebUserLocust(HttpLocust):
    # Speicify the weight of the locust.
    weight = 1
    # The taskset class name is the value of the task_set.
    task_set = UserBehavior
    # Wait time between the execution of tasks.
    min_wait = 5000
    max_wait = 15000


# This is another HttpLocust class.
class MobileUserLocust(HttpLocust):
    weight = 3
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000

# if __name__ == '__main__':
#     subprocess.Popen('locust -f .\locust_test_1.py --host=http://api.163.com', shell=True)
