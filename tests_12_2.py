import unittest
from runner_and_tournment import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        This method runs once before all tests in the class.
        It sets up the `all_results` dictionary to store the results of all tests.
        """
        cls.all_results = {}

    def setUp(self):
        """
        This method runs before each individual test.
        It initializes three Runner objects with different speeds:
        - Usain (speed 10)
        - Andrey (speed 9)
        - Nick (speed 3)
        """
        self.usain = Runner(name="Usain", speed=10)
        self.andrey = Runner(name="Andrey", speed=9)
        self.nick = Runner(name="Nick", speed=3)

    @classmethod
    def tearDownClass(cls):
        """
        This method runs once after all tests.
        It prints the `all_results` dictionary with results of all tests.
        """
        for test_number, results in cls.all_results.items():
            print(results)

    def test_race_usain_nick(self):
        """
        Test a race between Usain and Nick.
        Ensure that Nick comes last because of his slower speed.
        """
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.__class__.all_results[1] = {place: str(runner) for place, runner in results.items()}
        last_place_runner = results[max(results.keys())]
        self.assertTrue(last_place_runner.name == "Nick", "Nick should be the last runner.")

    def test_race_andrey_nick(self):
        """
        Test a race between Andrey and Nick.
        Ensure that Nick comes last.
        """
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results[2] = {place: str(runner) for place, runner in results.items()}
        last_place_runner = results[max(results.keys())]
        self.assertTrue(last_place_runner.name == "Nick", "Nick should be the last runner.")

    def test_race_usain_andrey_nick(self):
        """
        Test a race between Usain, Andrey, and Nick.
        Ensure that Nick comes last.
        """
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results[3] = {place: str(runner) for place, runner in results.items()}
        last_place_runner = results[max(results.keys())]
        self.assertTrue(last_place_runner.name == "Nick", "Nick should be the last runner.")


if __name__ == '__main__':
    unittest.main()