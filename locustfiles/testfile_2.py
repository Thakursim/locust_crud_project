import json
from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    wait_time = between(0,0.1)
    def on_start(self):
        # on_start is called when a Locust start before any task is scheduled.
        pass

    def on_stop(self):
        # on_stop is called when the TaskSet is stopping
        pass

    @task(1)
    def hello_world(self):
        self.client.get("/listing", name="/get_1st")

    @task
    def fill_crud(self):
        response = self.client.post('/api/fill_post/', {"number_1": 36, "number_2": 89, "number_3": 57, "text_4": "Sheesh"}, name="/post_1st")
        res = json.loads(response.text)
        put_id = (res['id'])
        self.client.put(f'/api/fill_post/{put_id}/', {"number_1": 76576, "number_2": 89657, "number_3": 5654, "text_4": "Sneha"}, name="/put_1st")
        self.client.patch(f'/api/fill_post/{put_id}/', {"text_4": "Suveksha"}, name="/patch_1st")
        self.client.delete(f'/api/fill_post/{put_id}/', name="/delete_1st")
   

    # @task(2)
    # def fill_post(self):
    #     print('post request')
    #     response = self.client.post('/api/fill_post/', {"number_1": 76, "number_2": 897, "number_3": 564, "text_4": "Sneha"})
    #     print(response.status_code)
    #     print(response.request)

    # @task(3)
    # def fill_put(self):
    #     print('put request')
    #     for id in range(2, 10):
    #         response = self.client.put(f'/api/fill_post/{id}/', {"text_4": "Sneha"})
    #         print(response.status_code)

    # @task(4)
    # def fill_patch(self):
    #     print('patch request')
    #     for id in range(2, 10):
    #         response = self.client.patch(f'/api/fill_post/{id}/', {"number_1": 76, "number_2": 897, "number_3": 564, "text_4": "Suveksha"})
    #         print(response.status_code)
    #         print(response.request)  

    # @task(1)
    # def fill_delete(self):
    #     print('delete request')
    #     for id in range(2, 10):
    #         response = self.client.delete(f'/api/fill_post/{id}/')
    #         print(response.status_code)
    #         print(response.request)      
