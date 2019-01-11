import unittest
from app.app import app
from flask import json

class useroperations(unittest.TestCase):
      client = app.test_client()
      users = {
         'user_id': "user_id",
         'firstname': "firstname",
         'lastname': "lastname",
         'othername': "othernames",
         'username': "username",
         'phonenumber': "phonenumber",
         'password': "password",
         'email': "email",
         'isAdmin': "isAdmin",
         'datetime.datetime.now()': "registeredon"   
      }
       
      user2 = {
          "email": "email",
          "password": "password"
      }
  
      def test_register_successfully(self):
      
         response = self.client.post('/api/v1/register', data=json.dumps(self.users), content_type='application/json')
         data = json.loads(response.data.decode())
         

      def test_name_missing(self):

         del self.users['username']
         response = self.client.post('/api/v1/register', data=json.dumps(self.users), content_type='application/json')
         data = json.loads(response.data.decode())
         

      def test_email_missing(self):
   
         del self.users['email']
         response = self.client.post('/api/v1/register', data=json.dumps(self.users), content_type='application/json')
         data = json.loads(response.data.decode())


      def test__login_successfully(self):
         
         response = self.client.post('/api/v1/login', data=json.dumps(self.user2), content_type='application/json')
         data = json.loads(response.data.decode())
     
      def test__email(self):
          
          del self.user2['password']
          response = self.client.post('/api/v1/login', data=json.dumps(self.user2), content_type='application/json')
          data = json.loads(response.data.decode())
   

      def test__password(self):
         del self.users['password']
         response = self.client.post('/api/v1/login', data=json.dumps(self.user2), content_type='application/json')
         data = json.loads(response.data.decode())



# class Redflag(BaseTestCase):
#    flag = {
#        'location': "Bwaise",
#        'type': "bribery",
#        'description': "a driver bribing a traffic police officer",
#        'media': "photo.jpg"
#     }
    
#    def test_redfag_created(self):

#       response = self.post('/api/v1/regflag', data=json.dumps(self.flag), content_type='application/json')
#       data = json.loads(response.data.decode())
#       print(data)
#       self.assertEqual('Redflag created', data['message'])
#       self.assertEqual(201, response.status_code)

     
    


if __name__ == '__main__':
   unittest.main()