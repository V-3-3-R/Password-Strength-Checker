# Unit Tests (run separately if needed)
class TestPasswordChecker(unittest.TestCase):
    def setUp(self):
        self.checker = AdvancedPasswordChecker()

    def test_weak_password(self):
        feedback = self.checker.check("weak")
        self.assertEqual(feedback.strength, "Weak")
        self.assertLess(feedback.score, 50)

    def test_strong_password(self):
        feedback = self.checker.check("CorrectHorseBatteryStaple42!")
        self.assertEqual(feedback.strength, "Strong")
        self.assertGreaterEqual(feedback.score, 80)

    def test_empty_password(self):
        with self.assertRaises(ValueError):
            self.checker.check("")

    def test_entropy_calculation(self):
        rule = EntropyRule()
        entropy = rule.calculate_entropy("abcABC123!")
        self.assertGreater(entropy, 30)  # Rough check

# To run tests:
suite = unittest.TestLoader().loadTestsFromTestCase(TestPasswordChecker); unittest.TextTestRunner(verbosity=2).run(suite)
