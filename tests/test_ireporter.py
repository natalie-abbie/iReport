import unittest
# from flask import Blueprint, Flask, request, json, jsonify, make_response, Response
from flask import redirect, jsonify, request, Response, json
from werkzeug.security import generate_password_hash, check_password_hash
from main.models.model import Redflag, FLAGS
from main.models.model import User
from main.views.users import SECRETKEY
import app
from main.views.users import loggedinuser
from main.views.users import USERS


class TestUser(unittest.TestCase):

    # def __init__():
    #     tear_down()
    @staticmethod
    def tear_down():
        global loggedinuser
        global USERS
        del loggedinuser[:]
        del USERS[:]

    def setUp(self):
        self.client = app.test_client()
        self.client.post('/api/v1/auth/register', content_type='application/json',
                         data=json.dumps({"firstname": "abio", "lastname": "nataline", "othername": "nats", "username": "talie", "password": "somepassword", "email": "abionatline@gmail.com", "phonenumber": "0752030815", "isAdmin": "true"}))

    def test_UserInstance(self):
        self.userObj1 = User(1, 'abio', 'natalie', 'nats', 'talie', 'abionatline@gmail.com',
                             '0752030815', generate_password_hash('password'), 'true')
        self.assertIsInstance(self.userObj1, User)

    def test_user_secret_key(self):
        pass
        global SECRETKEY
        result = 'TaLiEatalia'
        self.assertEqual(result, SECRETKEY)

    def test_user_registration_success(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"firstname": "abio", "lastname": "nataline", "othername": "nats", "username": "talie", "password": "somepassword", "email": "abionatline@gmail.com", "phonenumber": "0752030815", "isAdmin": "true"}))
        data = json.loads(response.data)
        self.assertEqual(201, response.status_code)
        self.assertEqual('Account created successfully', data['message'])

    def test_user_login_successful(self):
        response = self.client.post('/api/v1/auth/login', content_type='application/json',
                                    data=json.dumps({"username": "talie", "password": "somepassword"}))
        data = json.loads(response.data)
        self.assertEqual('logged in successfully', data['message'])
        self.assertEqual(200, response.status_code)

    def test_user_already_exists_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "talie", "password": "somepassword1", "email": "anotherperson@email.com"}))
        data = json.loads(response.data)
        self.assertEqual('user already exists', data['message'])
        self.assertEqual(400, response.status_code)

    def test_short_username_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "xxx", "password": "somepassword", "email": "some@email.com"}))
        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual(
            'username should be five characters and above', data['message'])

    def test_missing_username_user_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"email": "user@email.com", "password": "password"}))
        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual('username is missing', data['message'])

    def test_bad_email_format_user_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "personx", "email": "useremail.com", "password": "password"}))
        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual('email is invalid, @ symbol missing', data['message'])

    def test_missing_email_user_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "somepassword", "password": "somepassword"}))
        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual('email is missing', data['message'])

    def test_request_data_keys_user_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"userid": 1, "username": "fsfsf", "password": "somepassword", "email": "some@email.com"}))
        data = json.loads(response.data)
        self.assertTrue(400, response.status_code)
        self.assertNotEqual(4, data.keys())

    def test_user_login_failed_wrong_username(self):
        response = self.client.post('/api/v1/auth/login', content_type='application/json',
                                    data=json.dumps({"username": "tal", "password": "somepassword"}))
        data = json.loads(response.data)
        self.assertEqual(
            'unauthorised access, invalid username or password', data['message'])
        self.assertEqual(401, response.status_code)

    def test_user_login_failed_wrong_password(self):
        response = self.client.post('/api/v1/auth/login', content_type='application/json',
                                    data=json.dumps({"username": "talie", "password": "password"}))
        data = json.loads(response.data)
        self.assertIn(
            'unauthorised access, invalid username or password', data['message'])
        self.assertEqual(401, response.status_code)

    def test_already_loggedin_user(self):
        response = self.client.post('/api/v1/auth/login', content_type='application/json',
                                    data=json.dumps({"username": "talie", "password": "password"}))
        data = json.loads(response.data)
        self.assertEqual(401, response.status_code)
        self.assertEqual(
            'unauthorised access, invalid username or password', data['message'])


class TestRedflag(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.flagObj = Redflag(1, 1, 'Bribery', 'traffic police officer being bribere with money',
                               'abionatline@gmail.com', 'kyanja', 'nats')

        self.client.post('/api/v1/auth/register', content_type='application/json',
                         data=json.dumps({"firstname": "abio", "lastname": "nataline", "othername": "nats", "username": "talie", "password": "somepassword", "email": "abionatline@gmail.com", "phonenumber": "0752030815", "isAdmin": "true"}))

        self.client.post('/api/v1/auth/login', content_type='application/json',
                         data=json.dumps({"username": "talie", "password": "somepassword"}))

    def test_create_redflag_successful(self):
        response = self.client.post('/api/create_redflag', content_type='application/json',
                                    data=json.dumps({"type": "corruption", "description": "some description of the corruption", "email": "abionatline@gmail.com", "location": "kampala", "createdby": "nats"}))
        data = json.loads(response.data)
        self.assertEqual('flag successfully created', data['message'])
        self.assertTrue(400, response.status_code)

    def test_flag_already_exists(self):
        response = self.client.post('/api/flag', content_type='application/json',
                                    data=json.dumps({"type": "corruption", "description": "some description of the corruption", "email": "abionatline@gmail.com", "location": "kampala", "createdby": "nats"}))
        data = json.loads(response.data)
        self.assertEqual('flag successfully created', data['message'])
        self.assertTrue(201, response.status_code)

    def test_short_description_create_redflag(self):
        response = self.client.post('/api/flag', content_type='application/json',
                                    data=json.dumps({"type": "corruption", "description": "some ", "email": "abionatline@gmail.com", "location": "kampala", "createdby": "nats"}))
        data = json.loads(response.data)
        self.assertEqual(
            'name of flag should be well defined', data['message'])
        self.assertEqual(400, response.status_code)

    def test_type_missing_create_redflag(self):
        response = self.client.post('/api/flag', content_type='application/json',
                                    data=json.dumps({"description": "some description of the corruption", "email": "abionatline@gmail.com", "location": "kampala", "createdby": "nats"}))
        data = json.loads(response.data)
        self.assertEqual('flag type is missing', data['message'])
        self.assertEqual(400, response.status_code)

    def test_location_missing_create_redflag(self):
        response = self.client.post('/api/flag', content_type='application/json',
                                    data=json.dumps({"type": "corruption", "description": "some description of the corruption", "email": "abionatline@gmail.com", "createdby": "nats"}))
        data = json.loads(response.data)
        self.assertEqual('location is missing', data['message'])
        self.assertEqual(400, response.status_code)

    def test_createdby_missing_create_redflag(self):
        response = self.client.post('/api/v1/create_redflag', content_type='application/json',
                                    data=json.dumps({"type": "corruption", "description": "some description of the corruption", "email": "abionatline@gmail.com", "location": "kampala"}))
        data = json.loads(response.data)
        self.assertEqual('createdby is missing', data['message'])
        self.assertEqual(400, response.status_code)

    def test_description_missing_create_redflag(self):
        response = self.client.post('/api/flag', content_type='application/json',
                                    data=json.dumps({"type": "corruption", "email": "abionatline@gmail.com", "location": "kampala", "createdby": "nats"}))
        data = json.loads(response.data)
        self.assertEqual('description is missing', data['message'])
        self.assertEqual(400, response.status_code)

    def test_delete_flag_failed(self):
        response = self.client.delete(
            '/api/v1/redflag/<flag_id>', content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(
            'No flag has that id, nothing was deleted', data['message'])
        self.assertEqual(400, response.status_code)

    def test_update_flag_successful(self):
        response = self.client.put('api/v1/redflag/<flag_id>', content_type='application/json',
                                   data=json.dumps({'name': 'flagdemo', 'location': '', 'category': '', 'description': ''}))

        data = json.loads(response.data)
        self.assertEqual('no records of that flag exist', data['message'])
        self.assertEqual(404, response.status_code)


if __name__ == '__main__':
    unittest.main()
