import unittest
from runner_and_tournment import Runner, Tournament

# Define the decorator for skipping tests
def frozen_test_decorator(cls):
    """
    Decorator to conditionally skip tests based on the `is_frozen` attribute.
    """
    for attr_name in dir(cls):
        if attr_name.startswith('test_'):
            method = getattr(cls, attr_name)
            if callable(method):
                if getattr(cls, 'is_frozen', False):
                    setattr(cls, attr_name, unittest.skip('Тесты в этом кейсе заморожены')(method))
    return cls


@frozen_test_decorator
class RunnerTest(unittest.TestCase):
    """
    Unit tests for the Runner class.
    """
    is_frozen = False  # RunnerTest tests will run

    def test_walk(self):
        runner = Runner(name="Test Walker", speed=5)
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner(name="Test Runner", speed=10)
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 200)

    def test_challenge(self):
        walker = Runner(name="Walker", speed=5)
        runner = Runner(name="Runner", speed=10)
        for _ in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)


@frozen_test_decorator
class TournamentTest(unittest.TestCase):
    """
    Unit tests for the Tournament class.
    """
    is_frozen = True  # TournamentTest tests will be skipped

    def setUp(self):
        self.usain = Runner(name="Usain", speed=10)
        self.andrey = Runner(name="Andrey", speed=9)
        self.nick = Runner(name="Nick", speed=3)

    def test_first_tournament(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        last_place_runner = results[max(results.keys())]
        self.assertEqual(last_place_runner.name, "Nick")

    def test_second_tournament(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        last_place_runner = results[max(results.keys())]
        self.assertEqual(last_place_runner.name, "Nick")

    def test_third_tournament(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        last_place_runner = results[max(results.keys())]
        self.assertEqual(last_place_runner.name, "Nick")
