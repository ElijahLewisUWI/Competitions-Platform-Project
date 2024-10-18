import unittest
from werkzeug.security import generate_password_hash
from App.models import Student

class TestStudentFunctions(unittest.TestCase):
    
    # Test creation of a new student
    def test_new_student(self):
        new_student = Student(
            username="alice", 
            password=generate_password_hash("alicepass"), 
            firstName="Alice", 
            lastName="Smith", 
            email="alice@mail.com",
            studentID="S001" 
        )
        
        with self.subTest(msg="Testing student ID"):
            self.assertEqual(new_student.studentID, "S001")
        
        with self.subTest(msg="Testing username"):
            self.assertEqual(new_student.username, "alice")
        
        with self.subTest(msg="Testing first name"):
            self.assertEqual(new_student.firstName, "Alice")
        
        with self.subTest(msg="Testing last name"):
            self.assertEqual(new_student.lastName, "Smith")
        
        with self.subTest(msg="Testing email"):
            self.assertEqual(new_student.email, "alice@mail.com")
    #Test creation of converting to a dictionary 
    def test_to_dict(self):
        student = Student(
            username="alice",
            password=generate_password_hash("alicepass"),
            firstName="Alice",
            lastName="Smith",
            email="alice@mail.com",
            studentID="S001"  # Fixed studentID
        )
        
        student_dict = student.to_dict()
        
        self.assertDictEqual(student_dict, {
            'studentID': 'S001',            # Match the fixed studentID
            'firstName': 'Alice',            # Match the key from to_dict
            'lastName': 'Smith',             # Match the key from to_dict
            'email': 'alice@mail.com'        # Match the key from to_dict
        })

    def test_hashed_password(self):
        password = "alicepass"
        hashed = generate_password_hash(password, method='sha256')
        
        # Initialize the Student object with the hashed password
        student = Student(
            username="alice",
            password=hashed,
            firstName="Alice",
            lastName="Smith",
            email="alice@mail.com",
            studentID="S001"  # Fixed studentID
        )

        # Assert that the hashed password is not equal to the plain password
        self.assertNotEqual(student.password, password)

    def test_check_password(self):
        password = "alicepass"
        hashed = generate_password_hash(password, method='sha256')
        
        # Initialize the Student object with the hashed password
        student = Student(
            username="alice",
            password=hashed,
            firstName="Alice",
            lastName="Smith",
            email="alice@mail.com",
            studentID="S001"  # Fixed studentID
        )
        
        # Check if the password matches the hashed password
        self.assertTrue(student.check_password(password))
        

if __name__ == '__main__':
    unittest.main()
