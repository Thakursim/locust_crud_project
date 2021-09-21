import json
import string
import random
from locust import HttpUser, task, between


class Authentication(HttpUser):
    
    def registration_get_token(self):
        print('Authentication file post request')
        S = 6
        P = 10
        user = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
        print(user, 'USERNAME') 
        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = P))
        print(password, 'PASSWORD')
        response = self.client.post('/rest-auth/registration/', {"username": user, "password1": password, "password2": password})
        print(response.status_code)
        print(response.text, '-->resgistration token')
        res = json.loads(response.text)
        token = (res['key'])
        return token
