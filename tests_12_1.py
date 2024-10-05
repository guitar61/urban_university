from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Test Walker")
        for _ in range(10):
            runner.walk()
        # After 10 walks, the distance should be 50 (10 * 5)
        self.assertEqual(runner.distance, 50, "The distance after 10 walks should be 50")

    def test_run(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.run()
        # After 10 runs, the distance should be 100 (10 * 10)
        self.assertEqual(runner.distance, 100, "The distance after 10 runs should be 100")

    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        # After 10 runs for runner1 and 10 walks for runner2, their distances should not be equal
        self.assertNotEqual(runner1.distance, runner2.distance,
                            "Distances should not be equal after different activities")


if __name__ == '__main__':
    unittest.main()
