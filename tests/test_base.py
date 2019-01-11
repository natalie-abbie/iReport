from unittest import TestCase

class BaseTestCase(TestCase):
  def setUp(self):
      pass
   
    # self.app_context = self.app.app_context()
    # self.app_context.push()
    # self.client = self.app.test_client()

  def tearDown(self):
    # self.app = self.app_context.pop()
    pass
