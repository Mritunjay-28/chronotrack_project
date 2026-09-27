import unittest
from validator import parse_time, check_overlap

class TestChronoTrack(unittest.TestCase):

    def test_parse_valid_time(self):
        dt = parse_time("08:30")
        self.assertIsNotNone(dt)
        self.assertEqual(dt.hour, 8)
        self.assertEqual(dt.minute, 30)

    def test_parse_invalid_time(self):
        self.assertIsNone(parse_time("25:00"))
        self.assertIsNone(parse_time("random_text"))

    def test_time_order(self):
        err = check_overlap("10:00", "09:00", [])
        self.assertEqual(err, "Start time must be before end time.")

    def test_slot_overlap(self):
        existing = [{"id": 1, "title": "Gym", "start": "08:00", "end": "09:30", "status": "PENDING"}]
        err = check_overlap("09:00", "10:00", existing)
        self.assertIsNotNone(err)
        self.assertIn("Time conflict", err)

    def test_non_overlapping_slot(self):
        existing = [{"id": 1, "title": "Gym", "start": "08:00", "end": "09:30", "status": "PENDING"}]
        err = check_overlap("10:00", "11:00", existing)
        self.assertIsNone(err)

if __name__ == "__main__":
    unittest.main()