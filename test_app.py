import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from validation import vehicle_number
from main import main
from parking import show_slots


class ParkingSystemTests(unittest.TestCase):
    def test_valid_vehicle_number_format(self):
        self.assertTrue(vehicle_number("MP04BA4321"))
        self.assertFalse(vehicle_number("MP04BA432"))

    def test_registration_flow_accepts_valid_plate(self):
        with patch("builtins.input", side_effect=["1", "MP04BA4321", "1", "5"]):
            main()

    def test_show_slots_includes_vehicle_type(self):
        output = StringIO()
        with redirect_stdout(output):
            show_slots({"P1": "MP04BA4321"}, {"MP04BA4321": {"type": "Car"}})

        self.assertIn("MP04BA4321", output.getvalue())
        self.assertIn("Car", output.getvalue())


if __name__ == "__main__":
    unittest.main()
