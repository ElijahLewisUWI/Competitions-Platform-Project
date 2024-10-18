import unittest
from App.models import Results

class TestResultsFunctions(unittest.TestCase):

    # Test creation of new results entry
    def test_new_result(self):
        result = Results(
            resultID="R001",
            competitionID="C001",
            studentID="S001",
            score=85,
            completionTime="01:30:00",
            ranking=1
        )

        # Assertions to check the expected output
        self.assertEqual(result.resultID, "R001")
        self.assertEqual(result.competitionID, "C001")
        self.assertEqual(result.studentID, "S001")
        self.assertEqual(result.score, 85)
        self.assertEqual(result.completionTime, "01:30:00")
        self.assertEqual(result.ranking, 1)

    def test_to_dict(self):
        result = Results(
            resultID="R001",
            competitionID="C001",
            studentID="S001",
            score=85,
            completionTime="01:30:00",
            ranking=1
        )

        result_dict = result.to_dict()

        # Check that to_dict returns the expected dictionary
        expected_output = {
            "resultID": "R001",
            "competitionID": "C001",
            "studentID": "S001",
            "score": 85,
            "completionTime": "01:30:00",
            "ranking": 1
        }

        self.assertDictEqual(result_dict, expected_output)

if __name__ == '__main__':
    unittest.main()
