import json
import unittest

from tests import MockTestCase
from gyun.gomestor.connection import QSConnection


class TestGomeStorConnection(MockTestCase):

    connection_class = QSConnection

    def setUp(self):
        super(TestGomeStorConnection, self).setUp()
        self.conn = self.connection

    def test_connection_create_bucket(self):
        self.mock_http_response(status_code=201)
        bucket = self.conn.create_bucket(bucket="test-bucket", zone="pek3")
        self.assertEqual(bucket.name, "test-bucket")

    def test_connection_get_bucket(self):
        self.mock_http_response(status_code=200)
        bucket = self.conn.get_bucket(bucket="test-bucket")
        self.assertEqual(bucket.name, "test-bucket")

    def test_connection_get_all_buckets(self):
        body = {
            "count": 22,
            "buckets": [
                {
                    "location": "pek3",
                    "name": "test1",
                    "urls": [
                        "http://test1.gomestor.com",
                        "http://test1.pek3.gomestor.com",
                        "http://pek3.gomestor.com/test1"
                    ],
                    "created": "2015-10-15T15:08:19Z"
                }, {
                    "location": "pek3",
                    "name": "test0",
                    "urls": [
                        "http://test0.gomestor.com",
                        "http://test0.pek3.gomestor.com",
                        "http://pek3.gomestor.com/test0"
                    ],
                    "created": "2015-10-15T15:27:27Z"
                }]
        }

        self.mock_http_response(status_code=200, body=json.dumps(body))
        buckets = self.conn.get_all_buckets()
        self.assertDictEqual(buckets, body)

if __name__ == "__main__":
    unittest.main()
