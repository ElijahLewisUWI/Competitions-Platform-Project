import unittest
from datetime import date
from App.models import Competition

class TestCompetitionFunctions(unittest.TestCase):

    # Test creation of a new competition
    def test_new_competition(self):
        newcompetition = Competition(
            competitionID="C001",
            date=date(2024, 5, 10),
            title="Meteoroid Hackathon",  
            competitionType="Open",
            description="A programming competition",
            adminID="A001"
        )

        # Assertions to check the expected output
        self.assertEqual(newcompetition.competitionID, "C001")
        self.assertEqual(newcompetition.date, date(2024, 5, 10))
        self.assertEqual(newcompetition.title, "Meteoroid Hackathon")  
        self.assertEqual(newcompetition.competitionType, "Open")
        self.assertEqual(newcompetition.description, "A programming competition")
        self.assertEqual(newcompetition.adminID, "A001")

    def test_to_dict(self):
        # Creates a competition entry to convert to a dictionary 
        newcompetition = Competition(
            competitionID="C001",
            date=date(2024, 5, 10),
            title="Meteoroid Hackathon",  
            competitionType="Open",
            description="A programming competition",
            adminID="A001"
        )

        competition_dict = newcompetition.to_dict()

        # Check that to_dict returns the expected dictionary
        expected_output = {
            'competitionID': 'C001',
            'title': 'Meteoroid Hackathon',  
            'date': '2024-05-10',
            'description': 'A programming competition',
            'competitionType': 'Open',
            'adminID': 'A001',
        }

        self.assertDictEqual(competition_dict, expected_output)

if __name__ == '__main__':
    unittest.main()
