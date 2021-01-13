import unittest
import practice

class TestPractice(unittest.TestCase):

    def test_t_f(self):
        self.assertEqual(practice.t_f('t'), True, 'Should return True')
        self.assertEqual(practice.t_f('f'), False, 'Should return False')
    
    def test_tripler(self):
        self.assertEqual(practice.tripler(3), 9, 'Should return 9')
        self.assertEqual(practice.tripler(2), 6, 'Should return 6')
    
    def test_hundo(self):
        self.assertEqual(practice.hundo(100), "You dont enough money", 'Should return "You dont enough money"')
        self.assertEqual(practice.hundo(200), "Ballin", 'Should return "Ballin"')

if __name__ == '__main__':
    unittest.main()