"""Add your two tests here. Keep the supplied baseline and smoke tests intact."""
import unittest
from copy import deepcopy
from models import Booking
from service import move_booking

# Add a unittest.TestCase class with your two test methods.
# See IA 3.2 for the cases and the expectation you must record before using AI.

class MoveStudentTests(unittest.TestCase):
    # Given: a booking with no other blocker.
    # When: move a booking within the same room so its new interval overlaps its own old interval.
    # Expect: moving succeeds; the booking is updated with the new interval.

    # Given: a booking with no other blocker.
    # When: Request the booking's current room and times again.
    # Expect: An unchanged request succeeds without changing data.

    def test_move_overlapping_own_old_interval_succeeds(self):
        target = Booking(17, "Room 201", 600, 660)
        bookings = [target]
        result = move_booking(bookings, 17, "Room 201", 630, 690)

        self.assertIs(result, target)
        self.assertEqual(target, Booking(17, "Room 201", 630, 690))

    def test_unchanged_request_succeeds_without_changing_data(self):
        target = Booking(17, "Room 201", 600, 660)
        bookings = [target]
        before = deepcopy(bookings)
        result = move_booking(bookings, 17, "Room 201", 600, 660)

        self.assertIs(result, target)
        self.assertEqual(bookings, before)

if __name__ == "__main__":
    unittest.main()
