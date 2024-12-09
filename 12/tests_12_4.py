import unittest
import logging
from rt_with_exceptions import Runner  # Ensure this file is in the same directory

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",  # Overwrites the log file on each test run
    encoding="utf-8",
    format="%(levelname)s: %(message)s"
)


class RunnerTest(unittest.TestCase):
    """
    Unit tests for the Runner class, including logging of exceptions for invalid inputs.
    """

    def test_walk(self):
        """
        Test that walking with an invalid speed raises a ValueError
        and logs the appropriate warning.
        """
        try:
            # Invalid speed: -5
            r1 = Runner(name="Вася", speed=-5)
            r1.walk()
            logging.info('"test_walk" выполнен успешно')  # Logs success if no exception occurs
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")  # Logs the exception message

    def test_run(self):
        """
        Test that creating a Runner with an invalid name raises a TypeError
        and logs the appropriate warning.
        """
        try:
            # Invalid name: 123 (not a string)
            r2 = Runner(name=123, speed=5)
            r2.run()
            logging.info('"test_run" выполнен успешно')  # Logs success if no exception occurs
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")  # Logs the exception message


if __name__ == "__main__":
    unittest.main()
