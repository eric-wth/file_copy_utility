import unittest
import shutil
import os
from file_copy_utility import copy_file

class TestFileCopyUtility(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = "test_directory"
        os.makedirs(self.test_dir)

        # Create a test source file
        self.source_file = os.path.join(self.test_dir, "source.txt")
        with open(self.source_file, "w") as f:
            f.write("This is a test file.")

    def test_copy_file(self):
        # Define the destination file path
        destination_file = os.path.join(self.test_dir, "destination.txt")

        # Test file copying
        copy_file(self.source_file, destination_file)

        # Check if destination file exists and has the same content as source file
        self.assertTrue(os.path.exists(destination_file))
        with open(destination_file, "r") as f:
            self.assertEqual(f.read(), "This is a test file.")

    def tearDown(self):
        # Remove the temporary directory and its contents after testing
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

if __name__ == "__main__":
    unittest.main()
