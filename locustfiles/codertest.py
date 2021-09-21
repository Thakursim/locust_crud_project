import json
from locust import HttpUser, task, between
from authentication_test import Authentication

class CodeLocust(Authentication):
    wait_time = between(0,0.1)
    def on_start(self):
        self.token = self.registration_get_token()
        # on_start is called when a Locust start before any task is scheduled.
        pass

    def on_stop(self):
        # on_stop is called when the TaskSet is stopping
        pass

    @task
    def code_api_test(self):
        response = self.client.post('/api/coder/', {"developer": "Simran", "tester": "Ipshita", "infra_dev": 564}, headers = {'Authorization': 'Token {}'.format(self.token),}, name="/post_code")
        self.client.get('/api/coder', headers = {'Authorization': 'Token {}'.format(self.token),}, name="/get_code")
        
        res = json.loads(response.text)
        coder_id = (res['id'])
        self.client.put(f'/api/coder/{coder_id}/', {"developer": "Sanskriti", "tester": "Ishmita", "infra_dev": 4}, headers = {'Authorization': 'Token {}'.format(self.token),}, name="/put_code")
        self.client.patch(f'/api/coder/{coder_id}/', {"developer": "Suveksha"}, headers = {'Authorization': 'Token {}'.format(self.token),}, name="/patch_code")
        self.client.delete(f'/api/coder/{coder_id}/', headers = {'Authorization': 'Token {}'.format(self.token),}, name="/delete_code")
        
