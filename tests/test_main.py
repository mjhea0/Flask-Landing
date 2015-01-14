# tests/test_main.py


import unittest

from base import BaseTestCase
from project import db
from project.models import Email


class TestMainBlueprint(BaseTestCase):

    def test_index(self):
        # Ensure Flask is setup.
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sign up today to stay updated.', response.data)

    def test_add_email(self):
        # Ensure email can be added,
        with self.client:
            response = self.client.post(
                '/',
                data=dict(email="ad@min.com"),
                follow_redirects=True
            )
            self.assertIn('Thank you for your interest!', response.data)
            self.assertTrue(response.status_code == 200)

    def test_do_not_add_email(self):
        # Ensure poorly fomrmed email is not be added.
        with self.client:
            response = self.client.post(
                '/',
                data=dict(email="ad@min"),
                follow_redirects=True
            )
            self.assertIn('Invalid email address.', response.data)
            self.assertTrue(response.status_code == 200)

    def test_duplicate_emails(self):
        # Ensure emails are unique.
        email = Email('ad@min.com')
        db.session.add(email)
        db.session.commit()
        with self.client:
            response = self.client.post(
                '/',
                data=dict(email="ad@min.com"),
                follow_redirects=True
            )
            self.assertIn('Sorry that email aleady exists!', response.data)
            self.assertTrue(response.status_code == 200)


if __name__ == '__main__':
    unittest.main()
