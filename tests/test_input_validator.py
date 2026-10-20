import contextlib
import io
import unittest

from validation.input_validator import InputValidator


class InputValidatorTests(unittest.TestCase):

    def test_a_valid_command_is_split_and_lowercased(self):
        self.assertEqual(InputValidator().validate_command("  GO   East "), ["go", "east"])

    def test_bad_input_returns_an_empty_list(self):
        validator = InputValidator()

        with contextlib.redirect_stdout(io.StringIO()):      # "go" alone prints a hint
            for bad in ["", "dance", "go", "go up"]:
                self.assertEqual(validator.validate_command(bad), [], bad)


if __name__ == "__main__":
    unittest.main()
