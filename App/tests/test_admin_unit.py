import unittest
from werkzeug.security import generate_password_hash
from App.models import Admin

class TestAdminFunctions(unittest.TestCase):
    
    # Test creation of new admin
    def test_new_admin(self):
        newadmin = Admin(
            username="jane", 
            password=generate_password_hash("jane123"), 
            firstName="Jane", 
            lastName="Doe", 
            email="JaneDoe@mail.com",
            adminID="A001"
        )
        
        with self.subTest(msg="Testing username"):
            self.assertEqual(newadmin.username, "jane")
        
        with self.subTest(msg="Testing first name"):
            self.assertEqual(newadmin.firstName, "Jane")
        
        with self.subTest(msg="Testing last name"):
            self.assertEqual(newadmin.lastName, "Doe")
        
        with self.subTest(msg="Testing email"):
            self.assertEqual(newadmin.email, "JaneDoe@mail.com")
    
    def test_to_dict(self):
        admin = Admin(
            username="jane",
            password=generate_password_hash("jane123"),
            firstName="Jane",
            lastName="Doe",
            email="JaneDoe@mail.com",
            adminID="A001"
        )
        
        admin_dict = admin.to_dict()
        
        self.assertDictEqual(admin_dict, {
            'adminID': 'A001',          
            'firstName': 'Jane',        
            'lastName': 'Doe',          
            'email': 'JaneDoe@mail.com' 
        })


    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        admin = Admin(
            username="jane",
            password=hashed,
            firstName="Jane",
            lastName="Doe",
            email="JaneDoe@mail.com",
            adminID="A001"
        )

        # Assert that the hashed password is not equal to the plain password
        assert admin.password != password

    def test_check_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        
        # Initialize the Admin object with the hashed password
        admin = Admin(
            username="jane",
            password=hashed,
            firstName="Jane",
            lastName="Doe",
            email="JaneDoe@mail.com",
            adminID="A001"
        )
        
        # Check if the password matches the hashed password
        self.assertTrue(admin.check_password(password))

if __name__ == '__main__':
    unittest.main()
