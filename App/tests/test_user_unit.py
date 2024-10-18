import unittest
from werkzeug.security import generate_password_hash
from App.models import User

class TestUserFunctions(unittest.TestCase):

    # Test creation of a new user
    def test_new_user(self):
        newuser = User(
            username="bob",
            password=generate_password_hash("bobpass"),
            user_type="user",  
            firstName="Bob",
            lastName="Smith",
            email="bob@mail.com"
        )

        self.assertEqual(newuser.username, "bob")
        self.assertEqual(newuser.firstName, "Bob")
        self.assertEqual(newuser.lastName, "Smith")
        self.assertEqual(newuser.email, "bob@mail.com")
        self.assertEqual(newuser.user_type, "user")  

    def test_get_json(self):
        user = User(
            username="bob",
            password=generate_password_hash("bobpass"),
            user_type="user",
            firstName="Bob",
            lastName="Smith",
            email="bob@mail.com"
        )
        
        expected_json = {
            'id': None,  
            'username': 'bob'
        }
        self.assertDictEqual(user.get_json(), expected_json)

    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password)
        
        user = User(
            username="bob",
            password=hashed,
            user_type="user",
            firstName="Bob",
            lastName="Smith",
            email="bob@mail.com"
        )

        self.assertNotEqual(user.password, password)

    def test_check_password(self):
        password = "mypass"
        hashed = generate_password_hash(password)
        
        user = User(
            username="bob",
            password=hashed,
            user_type="user",
            firstName="Bob",
            lastName="Smith",
            email="bob@mail.com"
        )
        
        self.assertTrue(user.check_password(password))

if __name__ == '__main__':
    unittest.main()
