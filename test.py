import unittest
from flask_project_template.utils import *
import os



class Test(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(),'holi')

    def test_create_file(self):
        create_file('file_test')
        self.assertEqual(os.path.exists('file_test'), True)
        os.system('rm -rfd file_test')

    def test_create_dir(self):
        create_dir("dir_test")
        self.assertEqual(os.path.exists('dir_test'), True)
        os.system('rm -rfd dir_test')
    
    


if __name__ == "__main__":
    unittest.main()
