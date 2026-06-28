import unittest
from src import file_oper as fop
import os
import tempfile

class TestFileOperations(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, 'test.txt')
        with open(self.test_file, 'w') as f:
            f.write('hello')

    def tearDown(self):
        try:
            os.remove(self.test_file)
            os.rmdir(self.test_dir)
        except:
            pass

    def test_list_directory(self):
        contents = fop.list_directory(self.test_dir)
        self.assertIn('test.txt', contents)

    def test_create_folder(self):
        new_dir = os.path.join(self.test_dir, 'new_folder')
        result = fop.create_folder(new_dir)
        self.assertTrue(result)
        self.assertTrue(os.path.isdir(new_dir))
        os.rmdir(new_dir)

    def test_delete_file(self):
        result = fop.delete(self.test_file)
        self.assertTrue(result)
        self.assertFalse(os.path.exists(self.test_file))

    def test_delete_folder(self):
        new_dir = os.path.join(self.test_dir, 'new_folder')
        os.mkdir(new_dir)
        result = fop.delete(new_dir)
        self.assertTrue(result)
        self.assertFalse(os.path.exists(new_dir))

    def test_move(self):
        target_path = os.path.join(self.test_dir, 'moved.txt')
        result = fop.move(self.test_file, target_path)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(target_path))
        self.assertFalse(os.path.exists(self.test_file))
        # Возвращаем назад
        fop.move(target_path, self.test_file)

    def test_copy(self):
        copy_path = os.path.join(self.test_dir, 'copy.txt')
        result = fop.copy(self.test_file, copy_path)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(copy_path))
        os.remove(copy_path)

if __name__ == '__main__':
    unittest.main()