import unittest
from app.models import User
from app import db

class UserTestSuite(unittest.TestCase):

    def setUp(self):
        self.py = 3.14


    def tearDown(self):



    def test_create_user(self):
        newuser = User(username='Username_6',
                    email='Useremail_6@gmail.com',
                    password_hash='123123',
                    about_me="ABC")
        db.session.add(newuser)
        db.session.commit()
        user = User.query.filter_by(username=newuser.username).first()
        self.assertEqual(newuser.id, user.id)
        self.assertEqual(newuser.username, user.username)
        self.assertEqual(newuser.email, user.email)
        db.session.delete(user)
        db.session.commit()




    def test_read_user(self):
        user = User.query.get(1995)
        self.assertIsNotNone(user)


    def test_read_users(self):
        users = User.query.all()
        self.assertIsNotNone(users)


    def test_update_user(self):
        pass


    def test_delete_user(self):
        newUser = User(username='test_delete2',email='test_delete2@gmail.com',
                    password_hash='123321', about_me='ABC')
        db.session.add(newUser)
        db.session.commit()
        self.assertIsNotNone(newUser, "Created a new user.")
        user = User.query.get(newUser.id)
        db.session.delete(user)
        db.session.commit()

if __name__ == "__main__":
    unittest.main()
