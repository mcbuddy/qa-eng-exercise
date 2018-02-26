
import requests
import unittest
import MySQLdb, MySQLdb.cursors
import sys
import argparse
import datetime
import json

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.url = url
        self.conn = MySQLdb.connect(host=db_host, db=db_name, user=db_user)
        self.cursor = MySQLdb.cursors.DictCursor(self.conn)

    def test_get__all_users(self):
        resp = requests.get(self.url + '/users')
        data = resp.json()

        # db query
        self.cursor.execute("select count(*) from user ;")
        query = self.cursor.fetchone()

        # Assertion to count all user count between api and database
        self.assertEqual((query['count(*)']),(len(data['items'])))

    def test_get_user_with_id(self):
        id = '1'
        resp = requests.get(self.url + '/users/' + id)
        data = resp.json()
        # db query
        self.cursor.execute("select * from user where id = '" + id + "';")
        query = self.cursor.fetchone()

        # Assertion
        self.assertEqual(query['username'], data['username'])
        self.assertEqual(query['email'], data['email'])

    def test_create_new_user(self):
        # create unique user each test
        username = 'test' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        email = 'test' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '@test.com'
        headers = {'content-type': 'application/json'}
        payload = {"username":username, "email":email}

        resp = requests.post(self.url + '/users', data=json.dumps(payload), headers=headers)
        data = resp.json()

        # db query
        self.cursor.execute("select * from user where username = '" + username + "';")
        query = self.cursor.fetchone()

        # Assertion
        self.assertEqual(query['id'], data['id'])
        self.assertEqual(query['username'], data['username'])
        self.assertEqual(query['email'], data['email'])

    def tearDown(self):
        self.conn.close()

# define your testing env here by default it will be localhost:5000
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', default='local')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    if args.input == 'local':
        url = 'http://localhost:5000'
        db_host = 'localhost'
        db_name = 'exercise'
        db_user = 'root'
    elif args.input == 'qa':
        url = 'http://your-qa-server.com'
        db_host = 'your_db_server'
        db_name = 'db_name'
        db_user = 'db_user'
    else:
        raise ValueError('Wrong Environment selection, Please use qa or uat when using -i or --input=')

    sys.argv[1:] = args.unittest_args
    unittest.main()