"""
Unit test for CloudSync.
"""
import json
import os
import unittest

from src.cloud_sync import CloudSync


class TestCloudSync(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_progress.json'
        with open(self.test_file, 'w', encoding='utf-8') as f:
            json.dump({'beginner': ['Q1']}, f)
        self.sync = CloudSync(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_sync_to_cloud(self):
        self.sync.sync_to_cloud()
        self.assertEqual(self.sync.cloud_data, {'beginner': ['Q1']})

    def test_sync_from_cloud(self):
        self.sync.cloud_data = {'beginner': ['Q2']}
        self.sync.sync_from_cloud()
        with open(self.test_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertEqual(data, {'beginner': ['Q2']})

    def test_enable_collaboration(self):
        self.sync.enable_collaboration()
        # Just check that it runs without error

if __name__ == "__main__":
    unittest.main()
