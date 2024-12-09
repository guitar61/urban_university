import unittest
from tests_12_3 import RunnerTest, TournamentTest  # Import test cases

# Create a TestSuite
test_suite = unittest.TestSuite()

# Add RunnerTest and TournamentTest to the TestSuite
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Run the TestSuite with TextTestRunner
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)
