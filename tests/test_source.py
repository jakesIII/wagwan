import unittest
from app.models import Source_data

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source_data("Cnn","cnn","https:cnn.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source_data))