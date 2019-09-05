import unittest
import requests
import json
import yaml


class TestMethods(unittest.TestCase):

    GET_URL = "https://reqres.in/api/users"
    POST_URL = "https://reqres.in/api/users"

    def load_test_cases(self):
        stream = open("Data/CreateUser.yaml", 'r')
        dictionary = yaml.load(stream)
        return dictionary

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_Post_API(self):
        input_dict = self.load_test_cases()

        for input in input_dict:
            print input
            # json_file = open('Data/CreateUser.json', 'r')
            # json_data = json_file.read()
            # request = json.loads(json_data)
            request = {
                "name": input['name'],
                "job": input['job']
            }

            response = requests.post(self.POST_URL, request)

            self.assert_(response.status_code == 201)
            assert response.status_code, 201
            response_data = json.loads(response.content)

            assert response_data['name'] == input['name']
            assert response_data['job'] == input['job']
            assert response_data['createdAt'] is not None


if __name__ == '__main__':
    unittest.main()
