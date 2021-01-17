import unittest
from compass import Compass

class CompassTest(unittest.TestCase):

    def test_inc1_from_0_gives_1(self):
        compass = Compass(0)
        compass.inc()
        self.assertEqual(compass.degrees, 1)

    def test_inc10_from_0_gives_10(self):
        compass = Compass(0)
        compass.inc(interval=10)
        self.assertEqual(compass.degrees, 10)

    def test_inc1_from_1_gives_2(self):
        compass = Compass(1)
        compass.inc()
        self.assertEqual(compass.degrees, 2)

    def test_inc1_past_359_gives_0(self):
        compass = Compass(359)
        compass.inc()
        self.assertEqual(compass.degrees, 0)

    def test_inc10_past_359_gives_9(self):
        compass = Compass(359)
        compass.inc(interval=10)
        self.assertEqual(compass.degrees, 9)

    def test_inc359_from_0_gives_359(self):
        compass = Compass(359)
        compass.inc(interval=10)
        self.assertEqual(compass.degrees, 9)

    def test_inc359_from_1_gives_0(self):
        compass = Compass(359)
        compass.inc(interval=10)
        self.assertEqual(compass.degrees, 9)

    def test_inc359_from_359_gives_358(self):
        compass = Compass(359)
        compass.inc(interval=10)
        self.assertEqual(compass.degrees, 9)

    def test_override_degrees_from_10_to_20_and_inc1_gives_21(self):
        compass = Compass(10)
        compass.inc(currentDegrees=20)
        self.assertEqual(compass.degrees, 21)

    def test_interval_less_than_1_fails(self):
        compass = Compass()
        with self.assertRaises(ValueError) as context:
            compass.inc(interval=0)
        self.assertTrue("Interval must be higher than 0." in str(context.exception))

    def test_interval_more_than_359_fails(self):
        compass = Compass()
        with self.assertRaises(ValueError) as context:
            compass.inc(interval=360)
        self.assertTrue("Interval must be 359 or lower." in str(context.exception))



if __name__ == '__main__':
    unittest.main()
