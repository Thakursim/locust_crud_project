
import json
from locust import HttpUser, task, between

class SecondLocust(HttpUser):
    wait_time = between(0,0.1)
    def on_start(self):
        # on_start is called when a Locust start before any task is scheduled.
        pass

    def on_stop(self):
        # on_stop is called when the TaskSet is stopping
        pass

    @task(1)
    def hello_world(self):
        self.client.get("/listing", name="/get_2nd")

    @task
    def fill_crud(self):
        response = self.client.post('/api/fill_post/', {"number_1": 76, "number_2": 897, "number_3": 564, "text_4": "Sneha"}, name="/post_2nd")
        res = json.loads(response.text)
        put_id = (res['id'])
        self.client.put(f'/api/fill_post/{put_id}/', {"number_1": 76576, "number_2": 89657, "number_3": 5654, "text_4": "Sneha"}, name="/put_2nd")
        self.client.patch(f'/api/fill_post/{put_id}/', {"text_4": "Suveksha"}, name="/patch_2nd")
        self.client.delete(f'/api/fill_post/{put_id}/', name="/delete_2nd")
      
