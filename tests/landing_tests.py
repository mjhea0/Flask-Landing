import os
import unittest
from app import app, db
from app.module.models import Email
from config import _basedir, USERNAME, PASSWORD
from selenium import webdriver

DATABASE = 'test.db'
DATABASE_PATH = os.path.join(_basedir, DATABASE)
HOMEPAGE = 'http://localhost:9999/'

class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE_PATH
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_emptyDb(self):
        test = db.session.query(Email).all()
        assert len(test) == 0

    def test_addEmail(self):
        new_email = Email("michael@realpython.com")
        db.session.add(new_email)
        db.session.commit()
        test = db.session.query(Email).all()
        for t in test:
            t.email
        assert t.email == "michael@realpython.com"

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit

    def test_loginSuccess(self):
        self.driver.get(HOMEPAGE)
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_class_name('user').send_keys(USERNAME)
        self.driver.find_element_by_class_name('pass').send_keys(PASSWORD)
        self.driver.find_element_by_class_name("button").click()
        self.assertIn(HOMEPAGE + 'view', self.driver.current_url)

    def test_loginFailure(self):
        self.driver.get(HOMEPAGE)
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_class_name('user').send_keys('foo')
        self.driver.find_element_by_class_name('pass').send_keys('bar')
        self.driver.find_element_by_class_name("button").click()
        self.assertIn(HOMEPAGE + 'login', self.driver.current_url)

if __name__ == '__main__':
    unittest.main()

