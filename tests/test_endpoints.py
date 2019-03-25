# tests/test_endpoints.py


import json
import unittest

from app.models import Email
from tests.base import BaseTestCase


class TestApi(BaseTestCase):
    def test_api_sign_up(self):
        # Ensure email can be added through API
        test_email = 'test@email.com'
        with self.client:
            response = self.client.post(
                '/api/sign-up',
                content_type='application/json',
                json={'email': test_email}
            )
            self.assertEqual(response.status_code, 200)
            self.assertTrue(Email.query.filter(Email.email == test_email).first())
        # Ensure source can be added through API
        test_email = 'test1@email.com'
        source = 'somewebsite.com'
        with self.client:
            response = self.client.post(
                '/api/sign-up',
                content_type='application/json',
                json={'email': test_email, 'source': source}
            )
            self.assertEqual(response.status_code, 200)
            self.assertTrue(
                Email.query.filter(
                    Email.email == test_email,
                    Email.source == source
                ).first()
            )
        # Ensure form_data_as_json can be added through API
        test_email = 'peter.parker@pumpkineater.com'
        first_name, last_name = 'Peter', 'Parker'
        source = 'somewebsite.com'
        json_str = json.dumps({'first_name': first_name, 'last_name': last_name})
        with self.client:
            response = self.client.post(
                '/api/sign-up',
                content_type='application/json',
                json={
                    'email': test_email,
                    'source': source,
                    'form_data_as_json': json_str
                }
            )
            self.assertEqual(response.status_code, 200)
            self.assertTrue(
                    Email.query.filter(
                        Email.email == test_email,
                        Email.source == source,
                        Email.form_data_as_json == json_str
                    ).first()
            )

    def test_unique_contraint(self):
        # Ensure email with no source is not added twice
        test_email = 'test2@email.com'
        with self.client:
            response = self.client.post(
                '/api/sign-up',
                content_type='application/json',
                json={'email': test_email}
            )
            self.assertEqual(response.status_code, 200)
            self.assertTrue(Email.query.filter(Email.email == test_email).one())
        with self.client:
            response = self.client.post(
                '/api/sign-up',
                content_type='application/json',
                json={'email': test_email}
            )
            self.assertEqual(response.status_code, 200)
            self.assertTrue(Email.query.filter(Email.email == test_email).one())
        test_email = 'test3@email.com'
        source = 'the-source.com'
        with self.client:
            response = self.client.post(
                '/api/sign-up',
                content_type='application/json',
                json={'email': test_email, 'source': source}
            )
            self.assertEqual(response.status_code, 200)
            self.assertTrue(Email.query.filter(Email.email == test_email).one())
        with self.client:
            response = self.client.post(
                '/api/sign-up',
                content_type='application/json',
                json={'email': test_email, 'source': source}
            )
            self.assertEqual(response.status_code, 200)
            self.assertTrue(Email.query.filter(Email.email == test_email).one())


if __name__ == '__main__':
    unittest.main()
