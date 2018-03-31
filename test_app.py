import unittest
import os.path
import app

class TestApp(unittest.TestCase):

    def test_list_files(self):
        parent_path = os.path.abspath("test_media")
        result = app.list_files(parent_path)
        self.assertEqual(2, len(result))

if __name__ == '__main__':
    unittest.main()