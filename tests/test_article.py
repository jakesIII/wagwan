import unittest
from app.models import Articles_data

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Articles_data('abc','ABC','Ford','https:abc.com','urlimage','23-2-3-4')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Articles_data))